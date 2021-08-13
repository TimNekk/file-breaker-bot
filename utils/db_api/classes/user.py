from dataclasses import dataclass
from datetime import datetime

from utils.db_api.schemas import User


@dataclass
class UserData:
    created_at: datetime
    updated_at: datetime
    id: int
    uses: int
    banned: bool

    async def _update(self, **kwargs):
        await User.filter(id=self.id).update(**kwargs)

    async def add_uses_other(self, amount=1):
        self.uses += amount
        await self._update(uses=self.uses)

    async def ban(self):
        self.banned = True
        await self._update(banned=self.banned)

    async def unban(self):
        self.banned = False
        await self._update(banned=self.banned)
