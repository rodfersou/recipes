from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
Swagger(
    app,
    config={
        "specs_route": "/",
        "host": "0.0.0.0",
    },
    merge=True,
)


def get_app_with_views():
    from app.recipes.api import views  # noqa: F401

    return app


def start():
    app_with_views = get_app_with_views()
    app_with_views.run(
        debug=True,
    )
