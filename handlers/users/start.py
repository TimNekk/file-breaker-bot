from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api import db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await db.add_user(message.chat.id)

    await message.answer("""
Привет, я <b>Разрушитель файлов</b>! 💣

Отправь мне любой файл <i>(фото, видео, документ, песню и. д.)</i>
И я сделаю так, чтобы его невозможно было открыть!
""")
