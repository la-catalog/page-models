from datetime import datetime
from pydantic import BaseModel


class Metadata(BaseModel):
    created: datetime
    updated: datetime | None = None
    deleted: datetime | None = None
