#файл other.py
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from aiogram import types, Dispatcher
from create_bot import dp, bot
import json, string


# @dp.message_handler()
async def echo_send(message: types.Message):
    forbidden_words = json.load(open('cenz.json'))
    cleaned_words = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}

    intersection_result = cleaned_words.intersection(set(forbidden_words))
    print(intersection_result)

    if intersection_result:
        await message.reply('Маты запрещены')
        await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)