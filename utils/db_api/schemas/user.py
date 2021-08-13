from tortoise import fields

from utils.db_api.db_tortoise import TimedBaseModel


class User(TimedBaseModel):
    id = fields.BigIntField(pk=True)
    banned = fields.BooleanField(default=False)
    uses = fields.IntField(default=0)
