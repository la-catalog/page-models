from bson.objectid import ObjectId
from gtin import get_gcp, has_valid_check_digit
from pydantic import AnyUrl, BaseModel, conlist, constr, validator

from page_sku.attribute import Attribute
from page_sku.measurement import Measurement
from page_sku.metadata import Metadata
from page_sku.price import Price
from page_sku.rating import Rating


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
    variations: list[AnyUrl] = []
    sources: conlist(AnyUrl, min_items=1)
    links: list[AnyUrl] = []
    marketplace: constr(min_length=1, strip_whitespace=True)
    metadata: Metadata = Metadata()

    # To allow ObjectId type
    class Config:
        arbitrary_types_allowed = True

    @validator("gtin")
    def gtin_valid(value: str | None) -> str | None:
        if isinstance(value, str):
            assert has_valid_check_digit(value), "Invalid check digit"
            assert int(get_gcp(value)), "Invalid GCP"
        return value

    def json(self, *args, **kwargs) -> str:
        def _encoder(value):
            if isinstance(value, ObjectId):
                return str(value)

        kwargs["encoder"] = kwargs.get("encoder") or _encoder

        super().json(*args, **kwargs)
