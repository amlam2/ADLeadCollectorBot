import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет!</b>', parse_mode='html')

bot.polling(none_stop=True)
