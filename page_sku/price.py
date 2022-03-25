from pydantic import BaseModel, PositiveFloat, constr


class Price(BaseModel):
    amount: PositiveFloat | None = None
    currency: constr(min_length=1, strip_whitespace=True) | None = None
