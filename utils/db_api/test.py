import asyncio

import utils.db_api.db as commands
from utils.db_api.db_tortoise import on_startup

loop = asyncio.get_event_loop()


async def test():
    await on_startup()

    print('Очищаем таблицы')
    await commands.clear_tables()

    print("Добавляем пользователей")
    await commands.add_user(1)
    await commands.add_user(2)
    await commands.add_user(3)
    await commands.add_user(4)
    print("Готово")

    user = await commands.get_user(4)
    print(f"Получил пользователя: {user}")
    await user.add_uses()
    print(f"Обновил пользователя: {user}")
    await user.add_uses()
    print(f"Обновил пользователя: {user}")
    await user.ban()
    print(f"Обновил пользователя: {user}")
    await user.unban()
    print(f"Обновил пользователя: {user}")
    print("Тест успешный")


loop.run_until_complete(test())