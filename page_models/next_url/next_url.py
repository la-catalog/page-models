from pydantic import AnyHttpUrl, BaseModel, validator


class AnURL(BaseModel):
    url: AnyHttpUrl

    _url = validator("url", allow_reuse=True)(lambda u: str(u))
