from dataclasses import dataclass
from datetime import datetime

from aiogram.utils.exceptions import BotBlocked, ChatNotFound, BotKicked, UserDeactivated

from loader import dp
from utils.db_api.schemas import User


@dataclass
class UserData:
    created_at: datetime
    updated_at: datetime
    id: int
    uses: int
    banned: bool

    def __await__(self):
        return self._async_post_init().__await__()

    async def _async_post_init(self):
        await self.check_ban()

    async def _update(self, **kwargs):
        await User.filter(id=self.id).update(**kwargs)

    async def add_uses(self, amount=1):
        self.uses += amount
        await self._update(uses=self.uses)

    async def ban(self):
        self.banned = True
        await self._update(banned=self.banned)

    async def unban(self):
        self.banned = False
        await self._update(banned=self.banned)

    async def check_ban(self):
        try:
            await dp.bot.send_chat_action(self.id, 'typing')
        except (BotBlocked, ChatNotFound):
            await self.ban()
        except (UserDeactivated, BotKicked):
            await self.ban()
            await self.delete()

    async def delete(self):
        await User.filter(id=self.id).delete()
