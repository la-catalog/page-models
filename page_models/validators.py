from typing import Callable

from gtin import get_gcp, has_valid_check_digit

from page_models.url import URL

# I have to remember why i had the need to create this functions
# for some reason constr didn't solve my problem and i cant remember.
# I do remember that i had a big problem using "or" operation in types


def val_str(
    strip_whitespace: bool = False,
    to_lower: bool = False,
    to_upper: bool = False,
    min_length: int = None,
    max_length: int = None,
    ignore_classes: tuple = tuple(),
    ignore_values: tuple | list = tuple(),
) -> Callable[[str], str]:
    def func(string: str):
        if isinstance(string, ignore_classes):
            return string
        elif string in ignore_values:
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


def val_gtin(*args, **kwargs) -> Callable[[str], str]:
    def func(gtin: str):
        if not has_valid_check_digit(gtin):
            raise ValueError("invalid check digit")

        if not get_gcp(gtin).isnumeric():
            raise ValueError("invalid GCP")

        gtin = val_str(*args, **kwargs)(gtin)

        return gtin

    return func


def val_url(each_item: bool = False) -> Callable[[str | list[str]], str | list[str]]:
    if each_item:
        return lambda urls: [str(URL(url=url)) for url in urls]
    return lambda url: str(URL(url=url))
