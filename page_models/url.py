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
        # Pydantic can auto transforms str to URL
        # and in this cases it gives you the scheme.
        if "scheme" in kwargs:
            return super().__init__(url=url, *args, **kwargs)

        # If you are building an URL without Pydantic
        # this will let you do URL("https://www.google.com")
        scheme, found, _ = url.partition("://")

        if not found:
            raise ValueError(f"Scheme not found in '{url}'")

        super().__init__(url=url, scheme=scheme)
