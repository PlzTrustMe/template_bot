from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from peewee import SqliteDatabase

from infrastructure.database.dao.requests import RequestsDAO
from schemas.users import UserSchema


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, db: SqliteDatabase):
        self.db = db

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        dao = RequestsDAO(self.db)

        user_data: dict = {
            'user_id': event.from_user.id,
            'username': event.from_user.username,
            'full_name': event.from_user.full_name
        }

        user = dao.users.get_or_create(UserSchema(**user_data))

        data['dao'] = dao
        data['user'] = user

        return await handler(event, data)
