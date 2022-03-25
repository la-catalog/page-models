from pydantic import BaseModel, validator
from bson.objectid import ObjectId

from page_product.price import Price
from page_product.rating import Rating
from page_product.utility import string_not_empty, gtin_valid, url_valid, list_not_empty
from page_product.metadata import Metadata
from page_product.attribute import Attribute
from page_product.measurement import Measurement


class Product(BaseModel):
    _id: ObjectId = ObjectId()
    sku: str
    name: str
    brand: str | None = None
    description: str | None = None
    gtin: str | None = None
    prices: list[Price] = []
    segments: list[str] = []
    attributes: list[Attribute] = []
    measurement: Measurement = Measurement()
    package: Measurement = Measurement()
    rating: Rating = Rating()
    audios: list[str] = []
    images: list[str] = []
    videos: list[str] = []
    urls: list[str]
    marketplace: str
    metadata: Metadata

    _list_not_empty = validator("urls", allow_reuse=True)(list_not_empty)

    _string_not_empty = validator(
        "sku",
        "name",
        "brand",
        "description",
        "gtin",
        "marketplace",
        allow_reuse=True,
    )(string_not_empty)

    _strings_not_empty = validator("segments", "urls", allow_reuse=True, each_item=True)(
        string_not_empty
    )

    _urls_valid = validator(
        "urls", "audios", "images", "videos", allow_reuse=True, each_item=True
    )(url_valid)

    _gtin_valid = validator("gtin", allow_reuse=True)(gtin_valid)
