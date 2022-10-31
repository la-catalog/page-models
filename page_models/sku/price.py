from decimal import Decimal

from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.validators import val_number, val_str


@dataclass(config=core_config)
class Price(CoreModel):
    """
    SKU price (at cash or in installments).

    installments - Value of each installment
    currency - Installments currency (real, dollar euro, ...)
    method - Payment method (cash, credit, debit, pix, ...)

    Attention:
        at cash
            len(installments) == 1
        installments
            len(installments) > 1

    Why installments is a list? I cannot guarantee
    whenever all installments will have the same value
    (remember that this may be used to other countries).

    References:
        https://en.wikipedia.org/wiki/Decimal_data_type
        https://docs.python.org/3/library/decimal.html
        https://www.mongodb.com/docs/manual/tutorial/model-monetary-data/
    """

    installments: list[Decimal] = Field(default_factory=list, min_items=1)
    currency: str | None = Field(default=None)
    method: str | None = Field(default=None)

    _installments = validator("installments", allow_reuse=True)(
        val_number(positive=True, each_item=True)
    )

    _currency = validator("currency", allow_reuse=True)(
        val_str(
            strip_whitespace=True, to_lower=True, min_length=1, ignore_values=[None]
        )
    )

    _method = validator("method", allow_reuse=True)(
        val_str(
            strip_whitespace=True, to_lower=True, min_length=1, ignore_values=[None]
        )
    )
