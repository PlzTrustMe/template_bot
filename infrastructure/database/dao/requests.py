from dataclasses import dataclass

from peewee import SqliteDatabase

from infrastructure.database.dao.users import UserDAO


@dataclass
class RequestsDAO:
    db: SqliteDatabase

    @property
    def users(self) -> UserDAO:
        return UserDAO(self.db)
