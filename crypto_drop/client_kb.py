# файл client_kb
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove

b1 = KeyboardButton('/как_это_работает')
b2 = KeyboardButton('/поддержка')
b3 = KeyboardButton('/выбор_проекта')
b4 = KeyboardButton('/меню')
# b4 = KeyboardButton('поделиться номером', request_contact=True)
# b5 = KeyboardButton('отправить где я', request_location=True)


# kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b1, b2, b3)


kb_client = ReplyKeyboardMarkup() #этот класс замещает обычную клавиатуру на ту, что мы создаём 
kb_client.add(b1).add(b2).add(b3).add(b4) #.row(b4, b5)

