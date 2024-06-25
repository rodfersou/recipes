from typing import Optional, Self

import pydantic as pd

from app.base.models import Entity
from app.recipes.models import Recipe


class UpdateAPIRequest(Entity):
    title: Optional[str] = pd.Field(max_lengh=100, default=None)
    making_time: Optional[str] = pd.Field(max_lengh=100, default=None)
    serves: Optional[str] = pd.Field(max_lengh=100, default=None)
    ingredients: Optional[str] = pd.Field(max_lengh=100, default=None)
    cost: Optional[int] = None


class APIRequest(Entity):
    title: str = pd.Field(max_lengh=100)
    making_time: str = pd.Field(max_lengh=100)
    serves: str = pd.Field(max_lengh=100)
    ingredients: str = pd.Field(max_lengh=300)
    cost: int

    @classmethod
    def from_entity(cls, recipe: Recipe) -> Self:
        return cls(
            title=recipe.title,
            making_time=recipe.making_time,
            serves=recipe.serves,
            ingredients=recipe.ingredients,
            cost=recipe.cost,
        )


class APIResponse(APIRequest):
    id: int

    @classmethod
    def from_entity(cls, recipe: Recipe) -> Self:
        return cls(
            id=recipe.id,
            title=recipe.title,
            making_time=recipe.making_time,
            serves=recipe.serves,
            ingredients=recipe.ingredients,
            cost=recipe.cost,
        )
