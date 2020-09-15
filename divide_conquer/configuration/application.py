from flask import Flask
from flask_cors import CORS

from divide_conquer.entrypoints.rest.health import health_bp
from divide_conquer.entrypoints.rest.user import rest_user_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(rest_user_bp)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app
