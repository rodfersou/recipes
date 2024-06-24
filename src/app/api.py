from flask import Flask
from flasgger import Swagger


app = Flask(__name__)
Swagger(app, config={"specs_route": "/"}, merge=True)


def get_app_with_views():
    from app.recipes.api import views

    return app


def start():
    app_with_views = get_app_with_views()
    app_with_views.run(
        debug=True,
    )
