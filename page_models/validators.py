from numbers import Number
from typing import Any, Callable

from gtin import get_gcp, has_valid_check_digit

from page_models.url import URL


def should_ignore(
    value: Any, ignore_classes: tuple = tuple(), ignore_values: tuple | list = tuple()
) -> bool:
    """
    Check whenever the value should be ignored.

    Many validations accept exceptions and this functions
    is a shortcut to check this. For example, you may need to
    validate strings but you could also accept None values.
    """
    return isinstance(value, ignore_classes) or value in ignore_values


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
        if should_ignore(string, ignore_classes, ignore_values):
            return string

        if not isinstance(string, (str,)):
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


def val_gtin(
    strip_whitespace: bool = False,
    to_lower: bool = False,
    to_upper: bool = False,
    min_length: int = None,
    max_length: int = None,
    ignore_classes: tuple = tuple(),
    ignore_values: tuple | list = tuple(),
) -> Callable[[str], str]:
    def func(gtin: str):
        if should_ignore(gtin, ignore_classes, ignore_values):
            return gtin

        if not has_valid_check_digit(gtin):
            raise ValueError("Invalid check digit")

        if not get_gcp(gtin).isnumeric():
            raise ValueError("Invalid GCP")

        gtin = val_str(
            strip_whitespace=strip_whitespace,
            to_lower=to_lower,
            to_upper=to_upper,
            min_length=min_length,
            max_length=max_length,
            ignore_classes=ignore_classes,
            ignore_values=ignore_values,
        )(gtin)

        return gtin

    return func


def val_number(
    positive: bool = False,
    ignore_classes: tuple = tuple(),
    ignore_values: tuple | list = tuple(),
    each_item: bool = False,
) -> Callable[[Number], Number]:
    def func(number: Number):
        if should_ignore(number, ignore_classes, ignore_values):
            return number

        if not isinstance(number, Number):
            raise TypeError(f"Expected a number but received '{type(number)}'")

        if positive and number < 0:
            raise ValueError(f"Number {number} is not positive")

        return number

    if each_item:
        return lambda items: [func(i) for i in items]
    return func
