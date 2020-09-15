from uuid import uuid4

from sqlalchemy import Column, Date, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from divide_conquer.configuration.database import DatabaseBase
from divide_conquer.core.entity.user import User


class UserModel(DatabaseBase):
    __tablename__ = "user"

    user_id = Column("user_id", UUID(as_uuid=True), default=uuid4, primary_key=True)
    name = Column("name", String(50))
    nickname = Column("nickname", String(50), unique=True)
    birthday = Column("birthday", Date)
    created_at = Column("created_at", DateTime, default=func.now())

    def to_entity(self) -> User:
        return User(
            user_id=self.user_id,
            name=self.name,
            nickname=self.nickname,
            birthday=self.birthday,
            created_at=self.created_at,
        )
