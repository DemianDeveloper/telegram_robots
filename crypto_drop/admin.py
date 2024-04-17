# файл admin.py
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher


import os
import sys

id = None

# Путь к директории проекта в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from aiogram import types, Dispatcher
from create_bot import dp, bot
from data_base import sqlite_db
from data_base.sqlite_db import sql_add_command  
# from sqlite_db import sql_add_command

from keybords import admin_kb



class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def make_changes_command(message: types.Message):
    global id
    id = message.from_user.id
    chat_member = await message.chat.get_member(id)
    print(f"User {id} is a chat admin: {chat_member.status == 'administrator'}")
    await bot.send_message(message.from_user.id, 'Что хозяин надо?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='загрузить', state=None)
async def cm_start(message : types.Message):
    # if message.from_user.id == id:
    await FSMAdmin.photo.set()
    await message.reply('загрузить фото')


# выход из состояний
# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.reply('Операция отменена.')
    else:
        await message.reply('OK')

    
# ловим первый ответ и пишем в словарь 
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    # if message.from_user.id == id:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('теперь введи название')

# ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    # if message.from_user.id == id:
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('введи описание')

# ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    # if message.from_user.id == id:
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('теперь укажи цену')


# ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    try:
        # if message.from_user.id == id:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        await state.finish()
    except ValueError:
        await message.reply('Пожалуйста, введите корректное число для цены.')



# регистрируем хэндлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)