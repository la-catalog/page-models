from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel


@dataclass
class Rating(CoreModel):
    current: float | None = Field(default=None)
    min: float | None = Field(default=None)
    max: float | None = Field(default=None)
