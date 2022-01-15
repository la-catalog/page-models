from gtin import has_valid_check_digit, get_gcp
from schema import Schema, Or, And
from datetime import datetime
from bson.objectid import ObjectId

from page_product.utility import is_url, is_positive


def new_product() -> dict:
    return {
        "_id": str(ObjectId()),
        "sku": None,
        "name": None,
        "brand": None,
        "description": None,
        "gtin": None,
        "prices": [],
        "segments": [],
        "attributes": [],
        "measurement": {
            "width": None,
            "height": None,
            "length": None,
        },
        "package": {
            "width": None,
            "height": None,
            "length": None,
        },
        "rating": {
            "current": None,
            "min": None,
            "max": None,
        },
        "audios": [],
        "images": [],
        "videos": [],
        "url": None,
        "marketplace": None,
        "created": datetime.utcnow().isoformat(),
    }


def validate_product(product: dict):
    # Don't like Schema because it returns errors as string
    _validate_product_types(product)
    _validate_product_logic(product)


def _validate_product_types(product: dict):
    Schema(
        {
            "_id": str,
            "sku": str,
            "name": str,
            "brand": Or(str, None),
            "description": Or(str, None),
            "gtin": Or(str, None),
            "prices": [
                {
                    "amount": Or(float, None),
                    "currency": Or(str, None),
                }
            ],
            "segments": [str],
            "attributes": [
                {
                    "name": str,
                    "value": str,
                }
            ],
            "measurement": {
                "width": Or(float, None),
                "height": Or(float, None),
                "length": Or(float, None),
            },
            "package": {
                "width": Or(float, None),
                "height": Or(float, None),
                "length": Or(float, None),
            },
            "rating": {
                "current": Or(float, None),
                "min": Or(float, None),
                "max": Or(float, None),
            },
            "audios": [str],
            "images": [str],
            "videos": [str],
            "url": str,
            "marketplace": str,
            "created": str,
        }
    ).validate(product)


def _validate_product_logic(product: dict):
    Schema(
        {
            "_id": ObjectId.is_valid,
            "sku": len,
            "name": len,
            "brand": Or(len, None),
            "description": Or(len, None),
            "gtin": Or(And(len, has_valid_check_digit, get_gcp), None),
            "prices": [
                {
                    "amount": Or(is_positive, None),
                    "currency": Or(is_positive, None),
                }
            ],
            "segments": [
                len,
            ],
            "attributes": [
                {
                    "name": len,
                    "value": len,
                }
            ],
            "measurement": {
                "width": Or(is_positive, None),
                "height": Or(is_positive, None),
                "length": Or(is_positive, None),
            },
            "package": {
                "width": Or(is_positive, None),
                "height": Or(is_positive, None),
                "length": Or(is_positive, None),
            },
            "rating": {
                "current": Or(float, None),
                "min": Or(float, None),
                "max": Or(float, None),
            },
            "audios": [And(len, is_url)],
            "images": [And(len, is_url)],
            "videos": [And(len, is_url)],
            "url": And(len, is_url),
            "marketplace": len,
            "created": len,
        }
    ).validate(product)


p = new_product()
p["sku"] = "-"
p["name"] = "-"
p["url"] = "https://www.google.com"
p["marketplace"] = "https://www.google.com"
validate_product(p)
