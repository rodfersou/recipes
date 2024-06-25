from typing import Optional

import pydantic as pd

from app.base.models import Entity


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


class APIResponse(APIRequest):
    id: Optional[int]
