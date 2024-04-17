from aiogram import Bot, Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

os.environ['TOKEN'] = '6529585386:AAF7g4JqtOfBke4EW-UWslN088pdRxTLhtY'

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

def get_dispatcher():
    return dp
