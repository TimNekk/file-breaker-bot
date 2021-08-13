import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

from loader import dp, run_blocking_io
from utils.corrupting import corrupt_file
from utils.db_api import db


@dp.message_handler(content_types=['document'])
async def file_bot(message: types.Message, state: FSMContext):
    await state.set_state('file')

    file_name = f'user_files/{message.document.file_name}'
    try:
        await message.document.download(file_name)
    except FileNotFoundError:
        os.mkdir('user_files')

    await run_blocking_io(corrupt_file, file_name)

    await message.answer_document(InputFile(file_name), caption='Поврежденный файл')

    os.remove(file_name)

    user = await db.get_user(message.chat.id)
    await user.add_uses()

    await state.finish()