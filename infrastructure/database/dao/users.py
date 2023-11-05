from infrastructure.database.dao.base import BaseDAO
from infrastructure.database.models.user import User
from schemas.users import UserSchema


class UserDAO(BaseDAO):
    def get_or_create(self, user: UserSchema) -> User:
        with self.db.atomic():
            user, _ = User.get_or_create(**user.model_dump())

            return user
