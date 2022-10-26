from pydantic import Field, PositiveFloat, constr, validator
from pydantic.dataclasses import dataclass

from page_models.models import CoreModel
from page_models.validators import val_number, val_str


@dataclass
class Measurement(CoreModel):
    length: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)
    unit: str | None = Field(default=None)

    weight: float | None = Field(default=None)
    weight_unit: str | None = Field(default=None)

    _length = validator("length", allow_reuse=True)(val_number(positive=True))
    _width = validator("width", allow_reuse=True)(val_number(positive=True))
    _height = validator("height", allow_reuse=True)(val_number(positive=True))
    _unit = validator("unit", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _weight = validator("weight", allow_reuse=True)(val_number(positive=True))
    _weight_unit = validator("weight_unit", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )
