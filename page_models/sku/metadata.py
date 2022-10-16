from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, conint, conlist, validator


class Metadata(BaseModel):
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
    created: datetime = None
    updated: datetime = None
    deleted: datetime = None

    sources: conlist(AnyHttpUrl, min_items=1)
    query: str = None
    origin: str = None
    grade: conint(ge=0) = 0
    relatives: dict[str, bool] = {}
    links: list[AnyHttpUrl] = []

    hash: str = None

    _sources = validator("sources", each_item=True, allow_reuse=True)(lambda u: str(u))
    _links = validator("links", each_item=True, allow_reuse=True)(lambda u: str(u))

    def fill(self, hash: str):
        """
        Fill missing fields.

        Some fields shouldn't have None as value, but they
        can only be calculate after creating the SKU.
        """

        self.created = self.created or datetime.utcnow()
        self.updated = self.updated or self.created
        self.hash = hash
