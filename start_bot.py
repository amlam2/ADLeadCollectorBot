from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from database import sqlite_db


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


async def on_startup(_):
    print('Бот вышел в онлайн!')
    sqlite_db.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
