from pydantic import BaseModel, constr

from page_models.query.metadata import Metadata


class Query(BaseModel):
    query: constr(min_length=1, to_lower=True, strip_whitespace=True)
    metadata: Metadata = Metadata()

    class Config:
        json_encoders = {
            set: lambda v: list(v),
        }
