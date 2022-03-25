from gtin import has_valid_check_digit, get_gcp
from urllib.parse import urlsplit


def positive_number(value: float | None) -> float | None:
    if isinstance(value, float):
        assert value > 0, "Value must be positive"
    return value


def string_not_empty(value: str | None) -> str | None:
    if isinstance(value, str):
        value = value.strip()
        assert len(value) > 0, "String can not be empty"
    return value


def gtin_valid(value: str | None) -> str | None:
    if isinstance(value, str):
        assert has_valid_check_digit(value), "Invalid check digit"
        assert get_gcp(value), "Invalid GCP"
    return value


def url_valid(value: str) -> str:
    try:
        result = urlsplit(value)
    except Exception:
        raise ValueError("Invalid URL format")

    assert result.scheme in ("http", "https"), "URL doesn't start with http/https"

    return value
