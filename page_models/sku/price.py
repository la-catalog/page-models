from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel
from page_models.validators import val_number, val_str


@dataclass
class Price(CoreModel):
    value: float | None = Field(default=None)
    currency: str | None = Field(default=None)

    _value = validator("value", allow_reuse=True)(val_number(positive=True))
    _currency = validator("currency", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )
