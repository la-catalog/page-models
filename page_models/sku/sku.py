from hashlib import sha3_512

from pydantic import BaseModel, validator

from page_models.sku.attribute import Attribute
from page_models.sku.measurement import Measurement
from page_models.sku.metadata import Metadata
from page_models.sku.price import Price
from page_models.sku.rating import Rating
from page_models.validators import val_gtin, val_str, val_url


class SKU(BaseModel):
    """
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
    variations: list[str] | set[str] = []

    # Organization fields
    # Field used by organization to optimize pipeline or catalog
    metadata: Metadata

    class Config:
        json_encoders = {
            set: lambda v: list(v),
        }

    _code = validator("code", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _marketplace = validator("marketplace", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True, to_lower=True)
    )

    _name = validator("name", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _product = validator("product", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _brand = validator("brand", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _description = validator("description", allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _gtin = validator("gtin", allow_reuse=True)(
        val_gtin(min_length=8, strip_whitespace=True)
    )

    _ncm = validator("ncm", allow_reuse=True)(
        val_str(min_length=8, strip_whitespace=True)
    )

    _segments = validator("segments", each_item=True, allow_reuse=True)(
        val_str(min_length=1, strip_whitespace=True)
    )

    _audios = validator("audios", allow_reuse=True)(val_url(each_item=True))
    _images = validator("images", allow_reuse=True)(val_url(each_item=True))
    _videos = validator("videos", allow_reuse=True)(val_url(each_item=True))
    _variations = validator("variations", allow_reuse=True)(val_url(each_item=True))

    def get_core(self, *args, **kwargs) -> dict:
        """Get only the core fields."""

        sku = self.dict(*args, **kwargs)
        sku.pop("metadata", None)

        return sku

    def get_hash(self, *args, **kwargs) -> str:
        """
        Get the core fields hash.

        A hash is created from the core fields which
        tell us how the SKU was in that point in time.
        """

        sku = self.get_core(*args, **kwargs)
        data = str(sku).encode("UTF8")
        hash = sha3_512(data).hexdigest()

        return hash

    def fill(self):
        """
        Fill missing fields.

        Some fields shouldn't have None as value, but they
        can only be calculate after creating the SKU.
        """

        self.metadata.fill(hash=self.get_hash())

        return self
