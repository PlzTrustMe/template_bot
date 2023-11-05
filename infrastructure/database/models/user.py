from peewee import BigIntegerField, CharField

from .base import BaseModel, TimestampMixin


class User(BaseModel, TimestampMixin):
    user_id = BigIntegerField(primary_key=True, index=True)
    username = CharField(max_length=128, index=True, null=True)
    full_name = CharField(max_length=128)
