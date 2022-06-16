from pydantic import BaseModel, PositiveFloat, constr


class Price(BaseModel):
    value: PositiveFloat | None = None
    currency: constr(min_length=1, strip_whitespace=True) | None = None
