from typing import Optional

from app.base.models import Entity

import pydantic as pd


class RecipeAPI(Entity):
    title: str = pd.Field(max_lengh=100)
    making_time: str = pd.Field(max_lengh=100)
    serves: str = pd.Field(max_lengh=100)
    ingredients: str = pd.Field(max_lengh=300)
    cost: int


class RecipeAPIWithID(RecipeAPI):
    id: Optional[int]
