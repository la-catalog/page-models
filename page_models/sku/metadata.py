from datetime import datetime

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    created - When the SKU was created
    updated - When the SKU was last updated
    deleted - When the SKU was deleted

    query - The query which the SKU came from
    source - Who started this pipeline
    """

    created: datetime = datetime.utcnow()
    updated: datetime | None = None
    deleted: datetime | None = None
    query: str | None = None
    source: str | None = None
