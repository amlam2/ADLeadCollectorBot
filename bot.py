import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, '<b>И тебе привет!</b>', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'cat':
#         with open('cat.jpg', 'rb') as photo:
#             bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, message.text, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, '<b>Вау, крутое фото!</b>', parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://github.com'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website_ = types.KeyboardButton('Веб сайт')
    start_ = types.KeyboardButton('Запуск')
    markup.add(website_, start_)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


bot.polling(none_stop=True)
