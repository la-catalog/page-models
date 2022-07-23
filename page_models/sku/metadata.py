from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel, conint, conlist, constr, validator

from page_models.sku.snapshot import Snapshot


class Metadata(BaseModel):
    """
    created - When the SKU was created
    updated - When the SKU was last updated
    deleted - When the SKU was deleted

    sources - URLs used to create the SKU
    query - The query which the SKU came from
    origin - Who triggered the pipeline
    grade - Number representing the quality of the SKU
    snapshots - Snapshots from newer to oldest
    relatives - Code from SKUs related to the SKU
    links - Links to others SKUs (no related to this)
    """

    # Datetime fields (UTC time)
    created: datetime
    updated: datetime
    deleted: datetime | None = None

    sources: conlist(AnyHttpUrl, min_items=1)
    query: str | None = None
    origin: str | None = None
    grade: conint(ge=0) = 0
    snapshots: list[Snapshot] = []
    relatives: dict[str, bool] = {}
    links: list[AnyHttpUrl] = []

    _sources = validator("sources", each_item=True, allow_reuse=True)(lambda u: str(u))
    _links = validator("links", each_item=True, allow_reuse=True)(lambda u: str(u))
