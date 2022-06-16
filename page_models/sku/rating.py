from pydantic import BaseModel


class Rating(BaseModel):
    current: float | None = None
    min: float | None = None
    max: float | None = None
