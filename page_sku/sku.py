from bson.objectid import ObjectId
from gtin import get_gcp, has_valid_check_digit
from pydantic import AnyHttpUrl, BaseModel, conlist, constr, validator

from page_sku.attribute import Attribute
from page_sku.measurement import Measurement
from page_sku.metadata import Metadata
from page_sku.price import Price
from page_sku.rating import Rating


class SKU(BaseModel):
    id: ObjectId = ObjectId()
    product: ObjectId = ObjectId()
    code: constr(min_length=1, strip_whitespace=True)
    name: constr(min_length=1, strip_whitespace=True)
    brand: constr(min_length=1, strip_whitespace=True) | None = None
    description: constr(min_length=1, strip_whitespace=True) | None = None
    gtin: constr(min_length=8, strip_whitespace=True) | None = None
    ncm: constr(min_length=8, strip_whitespace=True) | None = None
    prices: list[Price] = []
    segments: list[constr(min_length=1, strip_whitespace=True)] = []
    attributes: list[Attribute] = []
    measurement: Measurement = Measurement()
    package: Measurement = Measurement()
    rating: Rating = Rating()
    audios: list[AnyHttpUrl] = []
    images: list[AnyHttpUrl] = []
    videos: list[AnyHttpUrl] = []
    variations: list[AnyHttpUrl] = []
    sources: conlist(AnyHttpUrl, min_items=1)
    links: list[AnyHttpUrl] = []
    marketplace: constr(min_length=1, strip_whitespace=True)
    metadata: Metadata = Metadata()

    class Config:
        fields = {"id": "_id"}  # Use alias with MongoDB
        arbitrary_types_allowed = True  # To allow ObjectId type
        json_encoders = {
            ObjectId: lambda v: str(v),
            set: lambda v: list(v),
        }

    @validator("gtin")
    def gtin_valid(value: str | None) -> str | None:
        if isinstance(value, str):
            assert has_valid_check_digit(value), "Invalid check digit"
            assert int(get_gcp(value)), "Invalid GCP"
        return value

    _audios = validator("audios", each_item=True, allow_reuse=True)(lambda u: str(u))
    _images = validator("images", each_item=True, allow_reuse=True)(lambda u: str(u))
    _videos = validator("videos", each_item=True, allow_reuse=True)(lambda u: str(u))
    _variations = validator("variations", each_item=True, allow_reuse=True)(
        lambda u: str(u)
    )
    _sources = validator("sources", each_item=True, allow_reuse=True)(lambda u: str(u))
    _links = validator("links", each_item=True, allow_reuse=True)(lambda u: str(u))
