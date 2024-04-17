# файл client.py
import os
import sys

# путь к директории проекта в PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from aiogram import types, Dispatcher
from create_bot import dp, bot  

from keybords import kb_client
from aiogram.types import ReplyKeyboardRemove

from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в CryptoDrop Fund!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/crypto_drop_test_bot')


# @dp.message_handler(commands=['как_это_работает'])
async def explain_how_it_works_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Объясняем как это работает:', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['поддержка'])
async def support_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'мы онлайн по графику: Пн-Вс с 9:00 до 20:00')


# @dp.message_handler(commands=['выбор_проекта'])
async def choose_project_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'вы направитесь в меню проекта')


# @dp.message_handler(commands=['меню'])
async def menu_command(message : types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(explain_how_it_works_command, commands=['как_это_работает'])
    dp.register_message_handler(support_open_command, commands=['поддержка'])
    dp.register_message_handler(choose_project_place_command, commands=['выбор_проекта'])
    dp.register_message_handler(menu_command, commands=['меню'])
