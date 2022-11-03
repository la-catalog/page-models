from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.validators import val_number, val_str, val_url


@dataclass(config=core_config)
class Audio(CoreModel):
    """
    Informations abouts the marketplace audio.

    url -  URL in the marketplace
    hash - Hash from the audio
    duration - Duration from the audio
    format - File format

    We don't store the URL used in our infrastructure,
    because there is no need for it. It's always possible
    to obtain the URL using the hash (and easy to switch
    to a new infrastructure). For example:

    https://www.gcp.com/audios/<HASH>
    https://www.amazon.com/aws/audios/<HASH>
    https://www.azure.com/18293494/audios/<HASH>
    """

    url: str
    hash: str = None
    duration: int = None
    format: str = None

    _url = validator("url", allow_reuse=True)(val_url())

    _hash = validator("hash", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )

    _duration = validator("duration", allow_reuse=True)(
        val_number(positive=True, ignore_values=[None])
    )

    _format = validator("format", allow_reuse=True)(
        val_str(strip_whitespace=True, min_length=1, ignore_values=[None])
    )
