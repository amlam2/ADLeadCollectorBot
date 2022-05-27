import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
# import os
import hashlib

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

answers = {}


# bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Кнопка-ссылка
urlKb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
buttonList = [
    InlineKeyboardButton(text='Ссылка3', url='https://google.com'),
    InlineKeyboardButton(text='Ссылка4', url='https://google.com'),
    InlineKeyboardButton(text='Ссылка5', url='https://google.com'),
]
urlKb.add(urlButton, urlButton2).row(*buttonList).insert(InlineKeyboardButton(text='Ссылка6', url='https://google.com'))
# urlKb.row(urlButton, urlButton2)

inKb = InlineKeyboardMarkup(row_width=1)
inButtonList = [
    InlineKeyboardButton(text='Like', callback_data='like_1'),
    InlineKeyboardButton(text='Dislike', callback_data='like_-1')
]
inKb.add(*inButtonList)


@dp.inline_handler()
async def inline_handler_cmd(query : types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        InlineQueryResultArticle(
            id = result_id,
            title = 'Статья Wikipedia:',
            url = link,
            input_message_content = InputTextMessageContent(message_text=link)
        )
    ]
    await query.answer(articles, cache_time=1, is_personal=True)


@dp.message_handler(commands=['ссылки'])
async def url_command(message : types.Message):
    await message.answer('Ссылочки:', reply_markup=urlKb)


@dp.message_handler(commands=['test'])
async def test_command(message : types.Message):
    await message.answer('Голосование за видео', reply_markup=inKb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
    # await callback.answer('Нажата инлайн кнопка')
    result = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answers:
        answers[f'{callback.from_user.id}'] = result
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)

    # await callback.message.answer('Нажата инлайн кнопка')
    # await callback.answer('Нажата инлайн кнопка', show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
