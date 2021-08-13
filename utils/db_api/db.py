from tortoise.exceptions import IntegrityError

from utils.db_api.classes import UserData
from utils.db_api.schemas import User


async def clear_tables():
    await User.all().delete()


async def add_user(user_id: int):
    try:
        return await User.create(id=user_id)
    except IntegrityError:
        pass


async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id).values()
    if user:
        return UserData(**user[0])
