from decimal import Decimal

from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel
from page_models.validators import val_number, val_str


@dataclass
class Price(CoreModel):
    """
    Represent the paying method for an item.

    installments - Value of each installment
    currency - Installments currency (real, dollar euro, ...)
    payment - Payment method (cash, credit, debit, pix, ...)

    References:
        https://en.wikipedia.org/wiki/Decimal_data_type
        https://docs.python.org/3/library/decimal.html
        https://www.mongodb.com/docs/manual/tutorial/model-monetary-data/
    """

    installments: list[Decimal] = Field(default_factory=list)
    currency: str | None = Field(default=None)
    payment: str | None = Field(default=None)

    _installments = validator("installments", allow_reuse=True)(
        val_number(positive=True, each_item=True)
    )

    _currency = validator("currency", allow_reuse=True)(
        val_str(
            strip_whitespace=True, to_lower=True, min_length=1, ignore_values=[None]
        )
    )

    _payment = validator("payment", allow_reuse=True)(
        val_str(
            strip_whitespace=True, to_lower=True, min_length=1, ignore_values=[None]
        )
    )
