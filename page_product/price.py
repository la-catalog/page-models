from pydantic import BaseModel, validator
from page_product.utility import positive_number, string_not_empty


class Price(BaseModel):
    amount: float | None = None
    currency: str | None = None

    _positive_number = validator("amount", allow_reuse=True)(positive_number)
    _string_not_empty = validator("currency", allow_reuse=True)(string_not_empty)
