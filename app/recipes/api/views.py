from flasgger import swag_from
from flask import request

from app.api import app
from app.recipes import handlers
from app.recipes.api import specs
from app.recipes.api.errors import override_errors
from app.recipes.api.models import APIRequest, APIResponse, UpdateAPIRequest


@app.route("/recipes", methods=["POST"])
@swag_from(specs.create_recipe)
@override_errors(
    {
        "message": "Recipe creation failed!",
        "required": "title, making_time, serves, ingredients, cost",
    }
)
def create_recipe() -> dict:
    api_request = APIRequest(**request.json)
    recipe = handlers.create_recipe(api_request)
    return {
        "message": "Recipe successfully created!",
        "recipe": [
            recipe.dict(),
        ],
    }


@app.route("/recipes")
@swag_from(specs.list_recipes)
@override_errors(
    {
        "message": "Recipe list failed!",
    }
)
def list_recipes() -> dict:
    return {
        "recipes": [
            APIResponse.from_entity(recipe).dict() for recipe in handlers.list_recipes()
        ],
    }


@app.route("/recipes/<int:recipe_id>")
@swag_from(specs.get_recipe)
@override_errors(
    {
        "message": "No recipe found",
    }
)
def get_recipe(recipe_id: int) -> dict:
    recipe = handlers.get_recipe(recipe_id)
    return {
        "message": "Recipe details by id",
        "recipe": [
            APIResponse.from_entity(recipe).dict(),
        ],
    }


@app.route("/recipes/<int:recipe_id>", methods=["PATCH"])
@swag_from(specs.update_recipe)
@override_errors(
    {
        "message": "Recipe update failed!",
        "required": "title, making_time, serves, ingredients, cost",
    }
)
def update_recipe(recipe_id: int) -> dict:
    api_request = UpdateAPIRequest(**request.json)
    recipe = handlers.update_recipe(recipe_id, api_request)
    return {
        "message": "Recipe successfully updated!",
        "recipe": [
            APIRequest.from_entity(recipe).dict(),
        ],
    }


@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
@swag_from(specs.delete_recipe)
@override_errors({"message": "No recipe found"})
def delete_recipe(recipe_id: int) -> dict:
    handlers.delete_recipe(recipe_id)
    return {
        "message": "Recipe successfully removed!",
    }
