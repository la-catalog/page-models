from typing import Callable

from gtin import get_gcp, has_valid_check_digit

from page_models.url import URL

"""
Why did i reinvent the wheel?

Whenever i used Pydantic functions (constr, conint, condate, condecimal, etc)
autocomplete was never able to infer the types and would say that my object
expect a value of type "Any". Example:

    class Foo(BaseModel):
        number: conint(gt=0)

    Foo(number=10)  # Autocomplete: (class) Foo(*, number: Any)

Other problem is that whenever i used Optional as type, the parameter
each_item from validator wouldn't see this as something to loop over. Example:

    class Foo(BaseModel):
        many_numbers: list[int] | set[int]

        @validator("many_numbers", each_item=True)
        def example(n: int):
            assert n >= 0
    
    Foo(many_numbers=[1, 2, 3, 4]) # Error

I'm considering using Data Classes (https://docs.python.org/3/library/dataclasses.html)
if pydantic doesn't add any value compared to @dataclass
"""


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
            raise ValueError(f"Minimum accepted length is {min_length}")

        if max_length is not None and len(string) > max_length:
            raise ValueError(f"Maximum accepted length is {min_length}")

        return string

    return func


def val_gtin(*args, **kwargs) -> Callable[[str], str]:
    def func(gtin: str):
        if not has_valid_check_digit(gtin):
            raise ValueError("Invalid check digit")

        if not get_gcp(gtin).isnumeric():
            raise ValueError("Invalid GCP")

        gtin = val_str(*args, **kwargs)(gtin)

        return gtin

    return func


def val_url(each_item: bool = False) -> Callable[[str | list[str]], str | list[str]]:
    if each_item:
        # I'm not preserving the iterator type, but is fine for me
        return lambda urls: [str(URL(url=url)) for url in urls]
    return lambda url: str(URL(url=url))


def val_number(positive: bool = False) -> Callable[[int | float], int | float]:
    def func(number: int | float):
        if not isinstance(number, (int, float)):
            raise TypeError(f"Expected a int or float but received '{type(number)}'")

        if positive and number < 0:
            raise ValueError(f"Number {number} is not positive")

        return number

    return func
