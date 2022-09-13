from hashlib import sha3_512

from pydantic import validator

from page_models.sku.base_sku import BaseSKU
from page_models.validators import val_gtin, val_str, val_url


class SKU(BaseSKU):
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

    _audios = validator("audios", each_item=True, allow_reuse=True)(val_url())
    _images = validator("images", each_item=True, allow_reuse=True)(val_url())
    _videos = validator("videos", each_item=True, allow_reuse=True)(val_url())
    _variations = validator("variations", each_item=True, allow_reuse=True)(val_url())

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
