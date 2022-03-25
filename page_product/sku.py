from gtin import has_valid_check_digit, get_gcp
from pydantic import BaseModel, AnyUrl, validator, constr, conlist
from bson.objectid import ObjectId

from page_product.price import Price
from page_product.rating import Rating
from page_product.metadata import Metadata
from page_product.attribute import Attribute
from page_product.measurement import Measurement


class SKU(BaseModel):
    _id: ObjectId = ObjectId()
    product: ObjectId = ObjectId()
    code: constr(min_length=1, strip_whitespace=True)
    name: constr(min_length=1, strip_whitespace=True)
    brand: constr(min_length=1, strip_whitespace=True) | None = None
    description: constr(min_length=1, strip_whitespace=True) | None = None
    gtin: constr(min_length=8, strip_whitespace=True) | None = None
    prices: list[Price] = []
    segments: list[constr(min_length=1, strip_whitespace=True)] = []
    attributes: list[Attribute] = []
    measurement: Measurement = Measurement()
    package: Measurement = Measurement()
    rating: Rating = Rating()
    audios: list[AnyUrl] = []
    images: list[AnyUrl] = []
    videos: list[AnyUrl] = []
    urls: conlist(AnyUrl, min_items=1)
    products: list[AnyUrl] = []
    links: list[AnyUrl] = []
    marketplace: constr(min_length=1, strip_whitespace=True)
    metadata: Metadata

    # To allow ObjectId type
    class Config:
        arbitrary_types_allowed = True

    @validator("gtin")
    def gtin_valid(value: str | None) -> str | None:
        if isinstance(value, str):
            assert has_valid_check_digit(value), "Invalid check digit"
            assert get_gcp(value), "Invalid GCP"
        return value
