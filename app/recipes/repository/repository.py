from datetime import datetime

from app.recipes.models import Recipe


class RecipeRepository:
    def _from_orm(self, recipe_sa) -> Recipe:
        pass

    def _to_orm(self, recipe: Recipe):
        pass

    def save(self, recipe: Recipe) -> Recipe:
        now = datetime.now()
        if not recipe.created_at:
            recipe.created_at = now
        recipe.updated_at = now
        if not recipe.id:
            recipe.id = 1
        return recipe
