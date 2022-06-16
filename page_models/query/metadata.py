from datetime import datetime

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    created - When the queyr was created
    """

    created: datetime = datetime.utcnow()
