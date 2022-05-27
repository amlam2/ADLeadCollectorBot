from aiogram import types, Dispatcher
from create_bot import dp
import json, string


# @dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('<b>Маты запрещены!</b>', parse_mode='html')
        await message.delete()
    else:
        # if message.text == 'Привет':
        #     await message.answer('И тебе привет!')
        await message.answer(message.text) # Просто отправляет сообщение
        # await message.reply(message.text) # Отправляет сообщение с упоминанием автора (сообщение в ответ)
        # await bot.send_message(message.from_user.id, message.text) # Отправляет сообщение в личку пользователю


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)
