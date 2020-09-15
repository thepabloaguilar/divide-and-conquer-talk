from punq import Container

from divide_conquer.core.use_case.user.create_new_user import (
    CreateNewUserUseCase,
    CreateNewUser,
)
from divide_conquer.dataproviders.database.user.repository import (
    CreateNewUserRepository,
)

di_container = Container()

# Dependencies
di_container.register(CreateNewUser, CreateNewUserRepository)

# Use Cases
di_container.register(CreateNewUserUseCase)
