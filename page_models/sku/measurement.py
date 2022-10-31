from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.validators import val_number, val_str


@dataclass(config=core_config)
class Measurement(CoreModel):
    """
    SKU/Package measurement.

    References:
        https://www.diferenca.com/comprimento-largura-e-altura/#:~:text=A%20norma%20diz%20que%20as,x%20altura%20(ou%20profundidade).
    """

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
