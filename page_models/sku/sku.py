from hashlib import sha3_512

from pydantic import AnyHttpUrl, Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.sku.attribute import Attribute
from page_models.sku.audio import Audio
from page_models.sku.image import Image
from page_models.sku.measurement import Measurement
from page_models.sku.metadata import Metadata
from page_models.sku.price import Price
from page_models.sku.rating import Rating
from page_models.sku.video import Video
from page_models.url import URL
from page_models.validators import val_gtin, val_str


@dataclass(config=core_config)
class SKU(CoreModel):
    """
    code - SKU code inside the marketplace (or any string that can be used as reference to SKU)
    marketplace - Marketplace name using snake_case style
    product - Product code inside the marketplace
    name - Name (never empty)
    brand - Brand
    description - Description
    gtin - Global Trade Item Number
    ncm - Nomeclatura comum do MERCOSUL
    segments - Segments from outermost to innermost
    attributes - Attributes without removing any field that is present in SKU
    measurement - Measures relative to the SKU (without being packaged)
    package - Measures after being packaged
    audios - Audios relative to SKU
    images - Images relative to SKU
    videos - Videos relative to SKU
    variations - URL to any variation

    prices - Prices with or without promotions
    rating - Review rating
    links - Links to others SKUs (no related to this)

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
    segments: list[str] = Field(default_factory=list)
    attributes: list[Attribute] = Field(default_factory=list)
    measurement: Measurement = Measurement()
    package: Measurement = Measurement()
    audios: list[Audio] = Field(default_factory=list)
    images: list[Image] = Field(default_factory=list)
    videos: list[Video] = Field(default_factory=list)
    variations: list[URL] = Field(default_factory=list)

    # Unstable fields
    # This fields represent a temporary information of the SKU in that marketplace,
    # they do not represent change in the SKU core information
    prices: list[Price] = Field(default_factory=list)
    rating: Rating = Rating()
    links: list[URL] = Field(default_factory=list)

    # Organization fields
    # Field used by organization to help pipeline or catalog
    metadata: Metadata = Field()

    _code = validator("code", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1)
    )

    _marketplace = validator("marketplace", allow_reuse=True)(
        val_str(strip_whitespace=True, to_lower=True, min_length=1)
    )

    _name = validator("name", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1)
    )

    _product = validator("product", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )

    _brand = validator("brand", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )

    _description = validator("description", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )

    _gtin = validator("gtin", allow_reuse=True)(
        val_gtin(min_length=8, strip_whitespace=True, ignore_values=[None])
    )

    _ncm = validator("ncm", allow_reuse=True)(
        val_str(min_length=8, strip_whitespace=True, ignore_values=[None])
    )

    _segments = validator("segments", each_item=True, allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1)
    )

    def get_core(self) -> dict:
        """Get only the core fields."""

        sku = self.dict()
        sku.pop("metadata", None)
        sku.pop("prices", None)
        sku.pop("rating", None)
        sku.pop("links", None)

        return sku

    def get_core_hash(self) -> str:
        """
        Get the core fields hash.

        A hash is created from the core fields which
        tell us how the SKU was in that point in time.
        """

        sku = self.get_core()
        data = str(sku).encode("UTF8")
        hash = sha3_512(data).hexdigest()

        return hash

    def get_prices_hash(self) -> str:
        """
        Get the prices field hash.

        A hash is created from the prices field which
        tell us the SKU prices in that point in time.
        """

        data = str(self.prices).encode("UTF8")
        hash = sha3_512(data).hexdigest()

        return hash

    def get_rating_hash(self) -> str:
        """
        Get the rating field hash.

        A hash is created from the rating field which
        tell us the SKU rating in that point in time.
        """

        data = str(self.rating).encode("UTF8")
        hash = sha3_512(data).hexdigest()

        return hash

    def __post_init_post_parse__(self):
        self.metadata.hash = self.get_core_hash()
