from pydantic import AnyHttpUrl, BaseModel, validator


class AnURL(BaseModel):
    """
    All pydantic URL objects require you to give the scheme when creating
    directly from them:
        AnyHttpUrl(url="https://www.example.com", scheme="https")
        AnyUrl(url="https://www.example.com", scheme="https")
        HttpUrl(url="https://www.example.com", scheme="https")
    But don't require while validating the type.

    This model exists so you can do:
        AnURL(url="https://www.example.com")
    """

    url: AnyHttpUrl

    _url = validator("url", allow_reuse=True)(lambda u: str(u))
