from pydantic import BaseModel


class Rating(BaseModel):
    current: float = None
    min: float = None
    max: float = None
