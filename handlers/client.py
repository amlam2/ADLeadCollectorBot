from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database.sqlite_db import sql_read


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/ADLeadCollectorBot')


# @dp.message_handler(commands=['Режим_работы'])
async def work_schedule(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def location(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная, д. 15', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Меню'])
async def menu_command(message : types.Message):
    await sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(work_schedule, commands=['Режим_работы'])
    dp.register_message_handler(location, commands=['Расположение'])
    dp.register_message_handler(menu_command, commands=['Меню'])
