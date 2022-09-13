from pydantic import BaseModel

from page_models.sku.attribute import Attribute
from page_models.sku.measurement import Measurement
from page_models.sku.metadata import Metadata
from page_models.sku.price import Price
from page_models.sku.rating import Rating


class BaseSKU(BaseModel):
    """
    Base SKU model, without enforcing any validation over the fields.

    Classes from others package may want to inherit most of the fields from SKU,
    but Pydantic doesn't let you remove the validation from fields. So if both classes
    use the same field name, it would be evaluted by both validators.
    More details: https://github.com/pydantic/pydantic/issues/1895

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
    """

    # Core fields
    # Any change to this fields, would mean that the SKU have been updated
    code: str
    marketplace: str
    name: str
    product: str = None
    brand: str = None
    description: str = None
    gtin: str = None
    ncm: str = None
    prices: list[Price] = []
    segments: list[str] = []
    attributes: list[Attribute] = []
    measurement: Measurement = Measurement()
    package: Measurement = Measurement()
    rating: Rating = Rating()
    audios: list[str] | set[str] = []
    images: list[str] | set[str] = []
    videos: list[str] | set[str] = []
    variations: list[str] = []

    # Organization fields
    # Field used by organization to optimize pipeline or catalog
    metadata: Metadata

    class Config:
        json_encoders = {
            set: lambda v: list(v),
        }
