import requests
import telebot
from telebot import types

from keyboards import news_keyboard, news_id_keyboard

bot = telebot.TeleBot('1720168371:AAHWOo67_-2Q5x2OvExhS_5rFHVGq8kVNFM')


def get_by_id(message):
    pk = message.text
    print(pk)
    data = requests.get(f'http://localhost:8000/api/products/{pk}').json()
    print(data)

    result = f"{data['title']}.\n\n{data['content']}\n"

    print(result)

    bot.send_message(message.chat.id, result)


def take_action(message):
    data = requests.get('http://localhost:8000/api/products/').json()
    result = ''

    keyboard = news_id_keyboard(message)

    action = message.text
    if action == 'News List':
        for i in data:
            result += f"{i['id']}. {i['title']}\n"
        print(result)

        bot.send_message(message.chat.id, result)
        bot.send_message(message.chat.id, "Batafsil oqish uchun yangilikning IDsini tanlang!", reply_markup=keyboard)
        bot.register_next_step_handler(message, get_by_id)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = news_keyboard(message)

    bot.send_message(message.chat.id, 'Let`s start')
    bot.send_message(message.chat.id, 'Choose the action:', reply_markup=keyboard)
    bot.send_message(964119166, message.from_user.first_name + ' is writing' + '\n message: ' + message.text)
    # bot.send_message(957096792, f"You are hacked by {message.from_user.first_name}")
    #
    # print(message)

    bot.register_next_step_handler(message, take_action)


bot.polling()
