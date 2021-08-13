from aiogram import types

from filters import IsAdmin
from loader import dp
from utils.db_api import db


@dp.message_handler(IsAdmin(), commands='is_ban_all')
async def is_ban_all_bot(message: types.Message):
    users = await db.get_users()

    for user in users:
        await user.check_ban()

    await message.answer('Чекнул')