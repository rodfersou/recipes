from flasgger import swag_from
from flask import request

from app.api import app
from app.recipes import handlers
from app.recipes.api import specs
from app.recipes.api.models import APIRequest, UpdateAPIRequest
from app.recipes.models import Recipe


@app.route("/recipes", methods=["POST"])
@swag_from(specs.create_recipe)
def create_recipe() -> tuple[dict, int]:
    api_request = APIRequest(**request.json)
    recipe = handlers.create_recipe(api_request)
    return {
        "message": "Recipe successfully created!",
        "recipe": [
            recipe.dict(),
        ],
    }, 200


@app.route("/recipes")
@swag_from(specs.list_recipes)
def list_recipes():
    return {
        "recipes": [recipe.dict() for recipe in handlers.list_recipes()],
    }, 200


@app.route("/recipes/<int:recipe_id>")
@swag_from(specs.get_recipe)
def get_recipe(recipe_id: int) -> tuple[dict, int]:
    recipe = handlers.get_recipe(recipe_id)
    return {
        "message": "Recipe details by id",
        "recipe": [
            recipe.dict(),
        ],
    }, 200


@app.route("/recipes/<int:recipe_id>", methods=["PATCH"])
@swag_from(specs.update_recipe)
def update_recipe(recipe_id: int) -> tuple[dict, int]:
    api_request = UpdateAPIRequest(**request.json)
    recipe = handlers.update_recipe(recipe_id, api_request)
    return {
        "message": "Recipe successfully updated!",
        "recipe": [
            recipe.dict(),
        ],
    }


@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
@swag_from(specs.delete_recipe)
def delete_recipe(recipe_id: int) -> tuple[dict, int]:
    handlers.delete_recipe(recipe_id)
    return {
        "message": "Recipe successfully removed!",
    }, 200
