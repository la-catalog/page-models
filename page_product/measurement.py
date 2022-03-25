from pydantic import BaseModel, PositiveFloat, constr


class Measurement(BaseModel):
    width: PositiveFloat | None = None
    height: PositiveFloat | None = None
    length: PositiveFloat | None = None
    unit: constr(min_length=1, strip_whitespace=True) | None = None

    weight: PositiveFloat | None = None
    weight_unit: constr(min_length=1, strip_whitespace=True) | None = None
