from datetime import datetime
from typing import Optional

from app.base.models import Entity

import pydantic as pd


class Recipe(Entity):
    id: Optional[int]
    title: str = pd.Field(max_lengh=100)
    making_time: str = pd.Field(max_lengh=100)
    serves: str = pd.Field(max_lengh=100)
    ingredients: str = pd.Field(max_lengh=300)
    cost: int
    created_at: datetime
    updated_at: datetime
