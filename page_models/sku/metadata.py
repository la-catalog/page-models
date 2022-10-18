from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, Field, conint, conlist, validator
from pydantic.dataclasses import dataclass, set_validation

from page_models.url import URL
from page_models.validators import val_url


@dataclass
class Metadata:
    """
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

    sources: list[str] = Field(default_factory=list, min_items=1)
    query: str = None
    origin: str = None
    grade: int = Field(default=0, ge=0)
    relatives: dict[str, bool] = Field(default_factory=dict)
    links: list[str] | set[str] = Field(default_factory=list)

    hash: str = None

    _sources = validator("sources", allow_reuse=True)(val_url(each_item=True))
    _links = validator("links", allow_reuse=True)(val_url(each_item=True))

    def fill(self, hash: str):
        """
        Fill missing fields.

        Some fields shouldn't have None as value, but they
        can only be calculate after creating the SKU.
        """

        self.hash = hash

    def __post_init_post_parse__(self):
        self.updated = self.updated or self.created
