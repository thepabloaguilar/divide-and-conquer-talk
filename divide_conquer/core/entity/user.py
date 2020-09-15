from datetime import date, datetime
from uuid import UUID

from pydantic.dataclasses import dataclass


@dataclass
class User:
    user_id: UUID
    name: str
    nickname: str
    birthday: date
    created_at: datetime
