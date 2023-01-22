from datetime import datetime

from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.url import URL
from page_models.validators import val_str


@dataclass(config=core_config)
class Metadata(CoreModel):
    """
    Metadata about SKU.

    created - When the SKU was created
    updated - When the SKU was last updated
    deleted - When the SKU was deleted

    sources - URLs used to create the SKU
    query - The query which the SKU came from
    origin - Who triggered the pipeline
    grade - Number representing the quality of the SKU
    relatives - Code from SKUs related to the SKU

    hash - Hash from core fields
    """

    # Datetime fields (UTC time)
    created: datetime = Field(default_factory=datetime.utcnow)
    updated: datetime = None
    deleted: datetime = None

    sources: list[URL] = Field(min_items=1)
    query: str = None
    origin: str = None
    grade: int = Field(default=0, ge=0)
    relatives: dict[str, bool] = Field(default_factory=dict)

    core_hash: str = None
    price_hash: str = None
    rating_hash: str = None

    _origin = validator("origin", allow_reuse=True)(
        val_str(min_length=1, to_upper=True, ignore_values=[None])
    )

    def __post_init_post_parse__(self):
        self.updated = self.updated or self.created
