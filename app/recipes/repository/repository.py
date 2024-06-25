from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app import config
from app.recipes.models import Recipe
from app.recipes.repository.orm import RecipeDB

engine = create_engine(config.ORM_URL, echo=config.DEBUG)


class RecipeRepository:
    def _from_db(self, recipe_db: RecipeDB) -> Recipe:
        return Recipe(
            id=recipe_db.id,
            created_at=recipe_db.created_at,
            updated_at=recipe_db.updated_at,
            title=recipe_db.title,
            making_time=recipe_db.making_time,
            serves=recipe_db.serves,
            ingredients=recipe_db.ingredients,
            cost=recipe_db.cost,
        )

    def _to_db(self, recipe: Recipe) -> RecipeDB:
        return RecipeDB(
            id=recipe.id,
            created_at=recipe.created_at,
            updated_at=recipe.updated_at,
            title=recipe.title,
            making_time=recipe.making_time,
            serves=recipe.serves,
            ingredients=recipe.ingredients,
            cost=recipe.cost,
        )

    def save(self, recipe: Recipe) -> Recipe:
        now = datetime.now()
        if not recipe.created_at:
            recipe.created_at = now
        recipe.updated_at = now

        with Session(engine) as session:
            recipe_db = self._to_db(recipe)
            session.add(recipe_db)
            session.commit()

            return self._from_db(recipe_db)

    def list(self) -> list[Recipe]:
        with Session(engine) as session:
            return [
                self._from_db(recipe_db) for recipe_db in session.query(RecipeDB).all()
            ]

    def get(self, recipe_id: int) -> Recipe:
        with Session(engine) as session:
            recipe_db = session.query(RecipeDB).filter_by(id=recipe_id).one()
            return self._from_db(recipe_db)
