from typing import Any

from bson.objectid import ObjectId
from gtin import get_gcp, has_valid_check_digit
from pydantic import AnyHttpUrl, BaseModel, conint, constr, validator

from page_models.sku.attribute import Attribute
from page_models.sku.measurement import Measurement
from page_models.sku.metadata import Metadata
from page_models.sku.price import Price
from page_models.sku.rating import Rating


class SKU(BaseModel):
    """
    id - Unique identifier for the document (ObjectId)
    code - SKU code inside the marketplace
    marketplace - Marketplace name using snake_case style

    product - Product code inside the marketplace
    name - Name (never empty)
    brand - Brand
    description - Description
    gtin - Global Trade Item Number
    ncm - Nomeclatura comum do MERCOSUL
    prices - Prices with or without promotions
    segments - Segments from outermost to innermost
    attributes - Attributes without removing any field that is present in SKU
    measurement - Measures relative to the SKU (without being packaged)
    package - Measures after being packaged
    rating - Review rating
    audios - Audios relative to SKU
    images - Images relative to SKU
    videos - Videos relative to SKU
    variations - URL to any variation

    metadata - Data that provides information about the SKU data
    links - Links to others SKUs (no related to this)
    """

    # Stable fields
    # Don't ever change
    id: ObjectId = ObjectId()
    code: constr(min_length=1, strip_whitespace=True)
    marketplace: constr(min_length=1, strip_whitespace=True, to_lower=True)

    # Core fields
    # Any change to this fields, would mean that the SKU have been updated
    product: constr(min_length=1, strip_whitespace=True) | None = None
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

    # Organization fields
    # Fields used by organization to optimize pipeline or catalog
    metadata: Metadata
    links: list[AnyHttpUrl] = []

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

    @validator("gtin")
    def gtin_valid(value: str) -> str:
        if isinstance(value, str):
            assert has_valid_check_digit(value), "Invalid check digit"
            assert int(get_gcp(value)), "Invalid GCP"
        return value

    _sku_id = validator("id", pre=True, allow_reuse=True)(object_id_valid)
    _audios = validator("audios", each_item=True, allow_reuse=True)(lambda u: str(u))
    _images = validator("images", each_item=True, allow_reuse=True)(lambda u: str(u))
    _videos = validator("videos", each_item=True, allow_reuse=True)(lambda u: str(u))
    _variations = validator("variations", each_item=True, allow_reuse=True)(
        lambda u: str(u)
    )

    _links = validator("links", each_item=True, allow_reuse=True)(lambda u: str(u))
