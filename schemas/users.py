from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    user_id: int
    username: Optional[str] = None
    full_name: str
