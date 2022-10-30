from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel
from page_models.validators import val_str


@dataclass
class Attribute(CoreModel):
    name: str = Field(default_factory=str)
    value: str = Field(default_factory=str)

    _name = validator("name", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1)
    )

    _value = validator("value", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1)
    )
