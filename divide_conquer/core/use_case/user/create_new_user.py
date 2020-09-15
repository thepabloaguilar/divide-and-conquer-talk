from abc import ABC, abstractmethod
from datetime import date

from pydantic.dataclasses import dataclass
from returns.result import ResultE

from divide_conquer.core.entity.user import User


@dataclass
class CreateNewUserCommand:
    name: str
    nickname: str
    birthday: date


class CreateNewUser(ABC):
    @abstractmethod
    def __call__(self, command: CreateNewUserCommand) -> ResultE[User]:
        pass


class CreateNewUserUseCase:
    def __init__(self, create_new_user: CreateNewUser) -> None:
        self._create_new_user = create_new_user

    def __call__(self, command: CreateNewUserCommand) -> ResultE[User]:
        return self._create_new_user(command)
