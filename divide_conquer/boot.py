from divide_conquer.configuration.application import create_app
from divide_conquer.configuration.database import init_db

application = create_app()


@application.cli.command("initdb")
def _init_db() -> None:
    init_db()


if __name__ == "__main__":
    application.run()
