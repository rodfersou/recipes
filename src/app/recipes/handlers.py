from app.recipes.api.models import RecipeAPI
from app.recipes.models import Recipe
from app.recipes.repository.repository import RecipeRepository


def create_recipe(api_request: RecipeAPI):
    repo = RecipeRepository()
    recipe = Recipe(
        title=api_request.title,
        making_time=api_request.making_time,
        serves=api_request.serves,
        ingredients=api_request.ingredients,
        cost=api_request.cost,
    )
    return repo.save(recipe)
