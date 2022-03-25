from pydantic import BaseModel, validator
from page_product.utility import positive_number, string_not_empty


class Measurement(BaseModel):
    width: float | None = None
    height: float | None = None
    length: float | None = None
    unit: str | None = None

    weight: float | None = None
    weight_unit: str | None = None

    _positive_number = validator(
        "width", "height", "length", "weight", allow_reuse=True
    )(positive_number)
    
    _string_not_empty = validator("unit", "weight_unit", allow_reuse=True)(
        string_not_empty
    )
