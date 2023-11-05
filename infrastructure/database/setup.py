from peewee import SqliteDatabase

from infrastructure.database.models.base import db
from infrastructure.database.models.user import User


def setup_database() -> SqliteDatabase:
    with db.atomic():
        db.create_tables([User])

        return db
