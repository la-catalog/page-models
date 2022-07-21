import unittest
from unittest import TestCase

from bson import ObjectId

from page_models import SKU


class TestID(TestCase):
    def setUp(self) -> None:
        self.objectid = ObjectId("62a576f61c248b5fdebbfc3b")
        self.sku = SKU(
            _id=self.objectid,
            name="foobar",
            code="123456",
            marketplace="test",
            metadata={"sources": ["https://www.thiagola92.com"]},
        )

        assert self.sku.id == self.objectid

    def test_id(self) -> None:
        dictionary = self.sku.dict()
        assert dictionary["id"] == self.sku.id

        dictionary["_id"] = dictionary.pop("id")
        sku = SKU.parse_obj(dictionary)
        assert sku.id == self.sku.id

    def test_id_alias(self) -> None:
        dictionary = self.sku.dict(by_alias=True)
        assert dictionary["_id"] == self.sku.id

        sku = SKU(**dictionary)
        assert sku.id == self.sku.id


if __name__ == "__main__":
    unittest.main()
