from pydantic import BaseModel
from typing import Union
from datetime import date


class Movies(BaseModel):
    title: str
    release_date: date
    imdb_rating: float
    description: Union[str, None] = None
