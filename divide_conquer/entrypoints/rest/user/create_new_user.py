from typing import Any, Union

from flask import Response
from flask_restful import Resource
from returns.result import Result

from divide_conquer.configuration.dependency_injection import di_container
from divide_conquer.core.entity.user import User
from divide_conquer.core.use_case.user.create_new_user import (
    CreateNewUserCommand,
    CreateNewUserUseCase,
)
from divide_conquer.entrypoints.rest.helpers import (
    json_response,
    unwrap_result_response,
    parse_request_body,
)


class CreateNewUserResource(Resource):
    API_PATH = "/users"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._create_new_user: CreateNewUserUseCase = di_container.resolve(
            CreateNewUserUseCase
        )

    @json_response
    @unwrap_result_response(success_status_code=201)
    @parse_request_body(CreateNewUserCommand)
    def post(
        self, request_body: Result[CreateNewUserCommand, Response]
    ) -> Result[User, Union[Response, Exception]]:
        return request_body.unify(self._create_new_user)
