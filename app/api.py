from flasgger import Swagger
from flask import Flask

from app import config

app = Flask(__name__)


def get_app_with_views():
    from app.recipes.api import views  # noqa: F401
    Swagger(app, config={
        "specs_route": config.SPECS_ROUTE,
        "host": config.HOST,
        "port": config.PORT,
    }, merge=True)
    return app


def start():
    app_with_views = get_app_with_views()
    app_with_views.run(debug=config.DEBUG)
