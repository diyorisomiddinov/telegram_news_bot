import requests
from telebot import types


def news_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    keyboard.add(types.KeyboardButton('News List'))
    return keyboard


def news_id_keyboard(message):
    data = requests.get('http://localhost:8000/api/products/').json()

    pks = []

    for i in data:
        pks.append(i['id'])

    keyboard = types.ReplyKeyboardMarkup(row_width=3)
       
    for i in pks:
        keyboard.add(types.KeyboardButton(i))

    return keyboard


                 # types.KeyboardButton('Get by id')