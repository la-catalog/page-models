import unittest
from unittest import TestCase

from page_models import SKU


class TestDate(TestCase):
    def test_created(self) -> None:
        """
        This test is s counter-measure for whenever someone change
            `created: datetime = None`
        to
            `created: datetime = datetime.utcnow()`

        Python will not rerun `utcnow()` whenever the object is created,
        so it needs to be calculated after the creating.
        """

        sku = SKU(
            code="test",
            marketplace="test",
            name="test",
            metadata={"sources": ["https://www.example.com"]},
        ).fill()

        sku2 = SKU(
            code="test",
            marketplace="test",
            name="test",
            metadata={"sources": ["https://www.example.com"]},
        ).fill()

        assert sku.metadata.created != sku2.metadata.created
        assert sku.metadata.updated != sku2.metadata.updated


if __name__ == "__main__":
    unittest.main()
