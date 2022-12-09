import unittest
from unittest import TestCase

from page_models.sku.metadata import Metadata


class TestSKUMetadata(TestCase):
    def test_dates(self) -> None:
        """
        Test dates.

        Multiple metadata shouldn't have the same "created" date.
        Empty "updated" date should be filled with the "created" date.
        """

        m1 = Metadata(sources=["https://www.example.com"], origin="test")
        m2 = Metadata(sources=["https://www.example.com"], origin="test")

        assert m1.created != m2.created
        assert m1.updated != m2.updated

        assert m1.created == m1.updated
        assert m2.created == m2.updated


if __name__ == "__main__":
    unittest.main()
