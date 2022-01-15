from urllib.parse import urlsplit

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
