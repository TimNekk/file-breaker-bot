from aiogram import types

from loader import dp


@dp.message_handler(content_types=['text', 'photo', 'video'])
async def any_bot(message: types.Message):
    addon = ''
    if message.content_type == 'photo':
        addon = 'это фото как '
    elif message.content_type == 'video':
        addon = 'это видео как '

    await message.answer(f'Отравь мне {addon}<b>файл</b>, чтобы я его сломал! 💣')
