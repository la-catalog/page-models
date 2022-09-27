from gtin import get_gcp, has_valid_check_digit

from page_models.url import URL


def val_str(
    strip_whitespace: bool = False,
    to_lower: bool = False,
    to_upper: bool = False,
    min_length: int = None,
    max_length: int = None,
    ignore_class: tuple = tuple(),
    ignore_value: tuple = tuple(),
) -> str:
    def func(string: str):
        if isinstance(string, ignore_class):
            return string
        elif string in ignore_value:
            return string
        elif not isinstance(string, (str,)):
            raise TypeError(f"Expected a string but received '{type(string)}'")

        if to_lower:
            string = string.lower()
        elif to_upper:
            string = string.upper()

        if strip_whitespace:
            string = string.strip()

        if min_length is not None and len(string) < min_length:
            raise ValueError(f"minimum accepted length is {min_length}")

        if max_length is not None and len(string) > max_length:
            raise ValueError(f"maximum accepted length is {min_length}")

        return string

    return func


def val_gtin(*args, **kwargs) -> str:
    def func(gtin: str):
        if not has_valid_check_digit(gtin):
            raise ValueError("invalid check digit")

        if not get_gcp(gtin).isnumeric():
            raise ValueError("invalid GCP")

        gtin = val_str(*args, **kwargs)(gtin)

        return gtin

    return func


def val_url(each_item: bool = False) -> str:
    if each_item:
        return lambda urls: [str(URL(url=url)) for url in urls]
    return lambda url: str(URL(url=url))
