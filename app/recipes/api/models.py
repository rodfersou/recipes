from typing import Optional

import pydantic as pd

from app.base.models import Entity


class RecipeAPI(Entity):
    title: str = pd.Field(max_lengh=100)
    making_time: str = pd.Field(max_lengh=100)
    serves: str = pd.Field(max_lengh=100)
    ingredients: str = pd.Field(max_lengh=300)
    cost: int


class RecipeAPIWithID(RecipeAPI):
    id: Optional[int]
