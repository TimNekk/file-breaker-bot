from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("""
Привет, я <b>Разрушитель файлов</b>! 💣

Отправь мне любой файл <i>(фото, видео, документ, песню и. д.)</i>
И я сделаю так, чтобы его невозможно было открыть!
""")
