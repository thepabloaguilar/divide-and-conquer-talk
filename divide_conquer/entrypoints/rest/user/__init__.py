from flask import Blueprint
from flask_restful import Api

from .create_new_user import CreateNewUserResource

rest_user_bp = Blueprint("rest_user", __name__)
rest_user_api = Api(rest_user_bp, prefix="/api")

rest_user_api.add_resource(CreateNewUserResource, CreateNewUserResource.API_PATH)
