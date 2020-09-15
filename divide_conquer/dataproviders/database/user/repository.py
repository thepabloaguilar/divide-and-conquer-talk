from returns.result import safe

from divide_conquer.configuration.database import database_session
from divide_conquer.core.entity.user import User
from divide_conquer.core.use_case.user.create_new_user import (
    CreateNewUser,
    CreateNewUserCommand,
)
from divide_conquer.dataproviders.database.user.model import UserModel


class CreateNewUserRepository(CreateNewUser):
    @safe
    def __call__(self, command: CreateNewUserCommand) -> User:
        user = UserModel(
            name=command.name, nickname=command.nickname, birthday=command.birthday,
        )

        with database_session() as session:
            session.add(user)
            session.commit()
            return user.to_entity()
