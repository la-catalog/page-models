from datetime import datetime

from pydantic import BaseModel


class Snapshot(BaseModel):
    hash: str
    date: datetime
