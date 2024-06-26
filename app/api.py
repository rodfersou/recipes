from flasgger import Swagger
from flask import Flask

from app import config

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error) -> tuple[dict, int]:
    return {"message": "Not Found"}, 404


def create_app():
    from app.recipes.api import views  # noqa: F401

    swagger_config = {
        "specs_route": config.SPECS_ROUTE,
    }
    Swagger(app, config=swagger_config, merge=True)
    return app


def start():
    app_with_views = create_app()
    app_with_views.run(debug=config.DEBUG)
