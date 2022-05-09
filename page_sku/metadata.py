from datetime import datetime

from pydantic import BaseModel


class Metadata(BaseModel):
    created: datetime = datetime.utcnow()
    updated: datetime | None = None
    deleted: datetime | None = None
