import unittest
from datetime import datetime
from unittest import TestCase

from bson import ObjectId

from page_models import SKU


class TestSnapshot(TestCase):
    def test_create_snapshot(self) -> None:
        sku = SKU(
            _id=ObjectId("62a576f61c248b5fdebbfc3b"),
            name="foobar",
            code="123456",
            marketplace="test",
            metadata={
                "created": datetime.utcnow(),
                "sources": ["https://www.thiagola92.com"],
            },
        )

        assert len(sku.metadata.snapshots) == 0

        sku.create_snapshot()

        assert len(sku.metadata.snapshots) == 1

        sku.create_snapshot()

        assert len(sku.metadata.snapshots) == 2
        assert sku.metadata.snapshots[0].hash == sku.metadata.snapshots[1].hash

        sku.name = "foobar2"
        sku.create_snapshot()

        assert len(sku.metadata.snapshots) == 3
        assert sku.metadata.snapshots[0].hash != sku.metadata.snapshots[2].hash


if __name__ == "__main__":
    unittest.main()
