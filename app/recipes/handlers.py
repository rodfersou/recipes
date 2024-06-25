from app.recipes.api.models import APIRequest, UpdateAPIRequest
from app.recipes.models import Recipe
from app.recipes.repository.repository import RecipeRepository


def create_recipe(api_request: APIRequest) -> Recipe:
    repo = RecipeRepository()
    recipe = Recipe(
        title=api_request.title,
        making_time=api_request.making_time,
        serves=api_request.serves,
        ingredients=api_request.ingredients,
        cost=api_request.cost,
    )
    return repo.save(recipe)


def list_recipes() -> list[Recipe]:
    repo = RecipeRepository()
    return repo.list()


def get_recipe(recipe_id: int) -> Recipe:
    repo = RecipeRepository()
    return repo.get(recipe_id)


def update_recipe(recipe_id: int, api_request: UpdateAPIRequest) -> Recipe:
    repo = RecipeRepository()
    return repo.update(
        recipe_id,
        api_request.dict(exclude_none=True),
    )


def delete_recipe(recipe_id: int):
    repo = RecipeRepository()
    return repo.delete(recipe_id)
