from pydantic import BaseModel


class Rating(BaseModel):
    curent: float | None = None
    min: float | None = None
    max: float | None = None
