from pydantic import validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.url import URL
from page_models.validators import val_number, val_str


@dataclass(config=core_config)
class Image(CoreModel):
    """
    Informations abouts the marketplace image.

    url -  URL in the marketplace
    hash - Hash from the image
    width - Width from the image (X axis)
    heigh - Height from the image (Y axis)
    format - File format

    We don't store the URL used in our infrastructure,
    because there is no need for it. It's always possible
    to obtain the URL using the hash (and easy to switch
    to a new infrastructure). For example:

    https://www.gcp.com/images/<HASH>
    https://www.amazon.com/aws/images/<HASH>
    https://www.azure.com/18293494/images/<HASH>
    """

    url: URL
    hash: str = None
    width: int = None
    height: int = None
    format: str = None

    _hash = validator("hash", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )

    _width = validator("width", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _height = validator("height", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _format = validator("format", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )
