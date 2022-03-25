from pydantic import BaseModel, validator
from page_product.utility import string_not_empty


class Attribute(BaseModel):
    name: str
    value: str

    _string_not_empty = validator("*", allow_reuse=True)(string_not_empty)
