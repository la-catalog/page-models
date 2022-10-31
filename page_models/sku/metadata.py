from datetime import datetime

from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.validators import val_url


@dataclass(config=core_config)
class Metadata(CoreModel):
    """
    Informations about the SKU.

    created - When the SKU was created
    updated - When the SKU was last updated
    deleted - When the SKU was deleted

    sources - URLs used to create the SKU
    query - The query which the SKU came from
    origin - Who triggered the pipeline
    grade - Number representing the quality of the SKU
    relatives - Code from SKUs related to the SKU
    links - Links to others SKUs (no related to this)

    hash - Hash from core fields
    """

    # Datetime fields (UTC time)
    created: datetime = Field(default_factory=datetime.utcnow)
    updated: datetime = None
    deleted: datetime = None

    sources: list[str] = Field(min_items=1)
    query: str = None
    origin: str = Field(min_length=1)
    grade: int = Field(default=0, ge=0)
    relatives: dict[str, bool] = Field(default_factory=dict)
    links: list[str] = Field(default_factory=list)

    hash: str = None

    _sources = validator("sources", allow_reuse=True)(val_url(each_item=True))
    _links = validator("links", allow_reuse=True)(val_url(each_item=True))

    def __post_init_post_parse__(self):
        self.updated = self.updated or self.created
