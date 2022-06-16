from typing import Any

from bson.objectid import ObjectId
from pydantic import AnyHttpUrl, BaseModel, conlist, constr, validator

from page_models.query.metadata import Metadata


class Query(BaseModel):
    id: ObjectId = ObjectId()
    query: constr(min_length=1, to_lower=True, strip_whitespace=True)
    metadata: Metadata = Metadata()

    class Config:
        fields = {"id": "_id"}  # Use alias with MongoDB
        arbitrary_types_allowed = True  # To allow ObjectId type
        json_encoders = {
            ObjectId: lambda v: str(v),
            set: lambda v: list(v),
        }

    def object_id_valid(value: Any) -> Any:
        if isinstance(value, str):
            return ObjectId(value)
        return value

    _sku_id = validator("id", pre=True, allow_reuse=True)(object_id_valid)
