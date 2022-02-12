from typing import Any
from urllib.parse import urlsplit


def skip_validation(object: Any):
    """
    No need to validate the logic of objects like "datetime" or "ObjectId",
    the logic is validated when you create the objects.
    """

    return True


def is_url(url: str):
    try:
        result = urlsplit(url)

        if result.scheme not in ("http", "https"):
            return False
    except:
        return False
    return True


def is_positive(number: float):
    return number > 0
