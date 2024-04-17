# файл bot_telegram.py
from aiogram import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import os
from data_base import sqlite_db

os.environ['TOKEN'] = '6529585386:AAF7g4JqtOfBke4EW-UWslN088pdRxTLhtY'

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

async def on_startup(dp: Dispatcher): #функция старта 
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    # bot.set_current()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
