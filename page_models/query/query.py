from pydantic import BaseModel, constr

from page_models.query.metadata import Metadata


class Query(BaseModel):
    query: constr(min_length=1, to_lower=True, strip_whitespace=True)
    metadata: Metadata = Metadata()

    class Config:
        json_encoders = {
            set: lambda v: list(v),
        }

    def fill(self):
        """
        Fill missing fields.

        Some fields shouldn't have None as value, but they
        can only be calculate after creating the SKU.
        """

        self.metadata.fill()

        return self
