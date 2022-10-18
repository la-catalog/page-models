from pydantic import AnyHttpUrl


class URL(AnyHttpUrl):
    """
    All pydantic URL objects require you to give the scheme when creating
    directly from them:
        AnyHttpUrl(url="https://www.example.com", scheme="https")
        AnyUrl(url="https://www.example.com", scheme="https")
        HttpUrl(url="https://www.example.com", scheme="https")

    This model exists so you can do:
        URL(url="https://www.example.com")
    """

    def __init__(self, url: str, *args, **kwargs) -> None:
        scheme, found, _ = url.partition("://")

        if not found:
            raise ValueError(f"Scheme not found in '{url}'")

        super().__init__(url=url, scheme=scheme, *args, **kwargs)
