from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.models import CoreModel
from page_models.validators import val_str


@dataclass
class Attribute(CoreModel):
    name: str = Field(default_factory=str)
    value: str = Field(default_factory=str)

    _name = validator("name", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _value = validator("value", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )
