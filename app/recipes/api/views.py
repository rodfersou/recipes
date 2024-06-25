from flasgger import swag_from
from flask import request

from app.api import app
from app.recipes import handlers
from app.recipes.api import specs
from app.recipes.api.models import RecipeAPI
from app.recipes.models import Recipe


@app.route("/recipes", methods=["POST"])
@swag_from(specs.create_recipe)
def create_recipe() -> tuple[dict, int]:
    recipe_request = RecipeAPI(**request.json)
    recipe = handlers.create_recipe(recipe_request)
    return {
        "message": "Recipe successfully created!",
        "recipe": [
            recipe.dict(),
        ],
    }


@app.route("/recipes")
@swag_from(specs.list_recipes)
def list_recipes():
    return {
        "recipes": [recipe.dict() for recipe in handlers.list_recipes()],
    }


@app.route("/recipes/<int:recipe_id>")
@swag_from(specs.get_recipe)
def get_recipe(recipe_id: int):
    recipe = handlers.get_recipe(recipe_id)
    return {
        "message": "Recipe details by id",
        "recipe": [
            recipe.dict(),
        ],
    }


@app.route("/recipes/<int:recipe_id>", methods=["PATCH"])
@swag_from(specs.update_recipe)
def update_recipe(recipe_id: int, recipe: Recipe):
    return recipe_id


@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
@swag_from(specs.delete_recipe)
def delete_recipe(recipe_id: int):
    return recipe_id
