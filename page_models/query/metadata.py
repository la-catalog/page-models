from datetime import datetime

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    created - When the queyr was created
    """

    # Datetime fields (UTC time)
    created: datetime = None

    def fill(self, hash: str):
        """Fill missing fields."""

        self.created = self.created or datetime.utcnow()
