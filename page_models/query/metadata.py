from datetime import datetime

from pydantic import BaseModel


class Metadata(BaseModel):
    """
    created - When the query was created
    """

    # Datetime fields (UTC time)
    created: datetime = None

    def fill(self):
        """
        Fill missing fields.

        Some fields shouldn't have None as value, but they
        can only be calculate after creating the SKU.
        """

        self.created = self.created or datetime.utcnow()
