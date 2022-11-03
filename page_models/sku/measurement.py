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

    length: float = None
    width: float = None
    height: float = None
    unit: str = None

    weight: float = None
    weight_unit: str = None

    _length = validator("length", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _width = validator("width", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _height = validator("height", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _unit = validator("unit", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True, ignore_values=[None])
    )

    _weight = validator("weight", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _weight_unit = validator("weight_unit", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True, ignore_values=[None])
    )
