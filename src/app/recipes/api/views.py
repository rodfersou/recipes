from flasgger import swag_from
from flask import request

from app.api import app
from app.recipes.api import specs
from app.recipes.models import Recipe


@app.route("/recipes/<int:recipe_id>", methods=["POST"])
@swag_from(specs.create_recipe)
def create_recipe(recipe: Recipe):
    return recipe_id


@app.route("/recipes")
@swag_from(specs.list_recipes)
def list_recipes():
    return []


@app.route("/recipes/<int:recipe_id>")
@swag_from(specs.get_recipe)
def get_recipe(recipe_id: int):
    return recipe_id


@app.route("/recipes/<int:recipe_id>", methods=["PATCH"])
@swag_from(specs.update_recipe)
def update_recipe(recipe_id: int, recipe: Recipe):
    return recipe_id


@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
@swag_from(specs.delete_recipe)
def delete_recipe(recipe_id: int):
    return recipe_id
