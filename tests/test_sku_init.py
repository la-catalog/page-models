import unittest
from unittest import TestCase

from page_models import SKU, Attribute, Image, Measurement, Metadata, Price, Rating


class TestSKUInit(TestCase):
    """
    Test initializing/creating a SKU.
    No need to get the information from a real SKU.
    """

    def setUp(self) -> None:
        self.code = "3616585721"
        self.marketplace = "americanas"
        self.product = "62b189331c248bcedf2d08b9"
        self.name = "Smartphone Motorola Edge 20 128GB 5G Wi-Fi Tela 6,7'' Dual Chip 8GB RAM Câmera Tripla + Selfie 32MP - Branco"
        self.brand = "MOTOROLA"
        self.description = "O mais avançado e potente"
        self.gtin = "7892597351206"
        self.price_obj = Price(installments=["2699"], currency="real", method="pix")
        self.price_dict = {
            "installments": ["2699"],
            "currency": "real",
            "method": "pix",
        }
        self.segments = [
            "celulares e smartphones",
            "smartphone",
            "motorola",
            "motorola edge 20",
        ]
        self.attribute_obj_1 = Attribute(name="Código", value="3616585721")
        self.attribute_obj_2 = Attribute(name="Código de barras", value="7892597351206")
        self.attribute_obj_3 = Attribute(name="Marca", value="MOTOROLA")
        self.attribute_obj_4 = Attribute(name="Tipo de Chip", value="Nano Chip")
        self.attribute_obj_5 = Attribute(name="Sistema Operacional", value="Android")
        self.attribute_obj_6 = Attribute(name="Tipo de Tela", value="POLED")
        self.attribute_dict_1 = {"name": "Código", "value": "3616585721"}
        self.attribute_dict_2 = {"name": "Código de barras", "value": "7892597351206"}
        self.attribute_dict_3 = {"name": "Marca", "value": "MOTOROLA"}
        self.attribute_dict_4 = {"name": "Tipo de Chip", "value": "Nano Chip"}
        self.attribute_dict_5 = {"name": "Sistema Operacional", "value": "Android"}
        self.attribute_dict_6 = {"name": "Tipo de Tela", "value": "POLED"}
        self.measurement_obj = Measurement(
            width=7.6, height=16.3, length=0.7, unit="cm", weight=163, weight_unit="g"
        )
        self.measurement_dict = {
            "width": 7.6,
            "height": 16.3,
            "length": 0.7,
            "unit": "cm",
            "weight": 163,
            "weight_unit": "g",
        }
        self.rating_obj = Rating(current=4.2, min=1, max=5)
        self.rating_dict = {"current": 4.2, "min": 1, "max": 5}
        self.images_obj = [
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_1SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_2SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_3SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_4SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_5SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_6SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_7SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_8SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_9SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_10SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_11SZ.jpg"
            ),
            Image(
                url="https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_12SZ.jpg"
            ),
        ]
        self.images_dict = [
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_1SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_2SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_3SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_4SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_5SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_6SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_7SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_8SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_9SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_10SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_11SZ.jpg"
            },
            {
                "url": "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_12SZ.jpg"
            },
        ]
        self.metadata_obj = Metadata(
            origin="test", sources=["https://www.americanas.com.br/produto/3616585721"]
        )
        self.metadata_dict = {
            "origin": "test",
            "sources": ["https://www.americanas.com.br/produto/3616585721"],
        }

    def test_sku_from_objects(self) -> None:
        """
        Test creating SKU using Python objects.

        Advantage: Python object provide the developer with autocomplete.
        """

        self.sku = SKU(
            code=self.code,
            marketplace=self.marketplace,
            product=self.product,
            name=self.name,
            brand=self.brand,
            description=self.description,
            gtin=self.gtin,
            prices=[self.price_obj],
            segments=self.segments,
            attributes=[
                self.attribute_obj_1,
                self.attribute_obj_2,
                self.attribute_obj_3,
                self.attribute_obj_4,
                self.attribute_obj_5,
                self.attribute_obj_6,
            ],
            measurement=self.measurement_obj,
            rating=self.rating_obj,
            images=self.images_obj,
            metadata=self.metadata_obj,
        )

    def test_sku_from_dict(self) -> None:
        """
        Test creating SKU using Python dictionaries.

        Advantage: Easily import docs from Mongo/Rabbit/Serialized.
        """

        self.sku = SKU(
            **{
                "code": self.code,
                "marketplace": self.marketplace,
                "product": self.product,
                "name": self.name,
                "brand": self.brand,
                "description": self.description,
                "gtin": self.gtin,
                "prices": [self.price_dict],
                "segments": self.segments,
                "attributes": [
                    self.attribute_dict_1,
                    self.attribute_dict_2,
                    self.attribute_dict_3,
                    self.attribute_dict_4,
                    self.attribute_dict_5,
                    self.attribute_dict_6,
                ],
                "measurement": self.measurement_dict,
                "rating": self.rating_dict,
                "images": self.images_dict,
                "metadata": self.metadata_dict,
            }
        )

    def test_sku_from_hybrid(self) -> None:
        """
        Test creating SKU using Python object and dictionaries.

        Advantage: None?
        """

        self.sku = SKU(
            code=self.code,
            marketplace=self.marketplace,
            product=self.product,
            name=self.name,
            brand=self.brand,
            description=self.description,
            gtin=self.gtin,
            prices=[self.price_dict],
            segments=self.segments,
            attributes=[
                self.attribute_dict_1,
                self.attribute_dict_2,
                self.attribute_dict_3,
                self.attribute_dict_4,
                self.attribute_dict_5,
                self.attribute_dict_6,
            ],
            measurement=self.measurement_dict,
            rating=self.rating_dict,
            images=self.images_dict,
            metadata=self.metadata_dict,
        )

    def tearDown(self) -> None:
        """Check if transforming is still working"""

        assert self.sku.json()
        assert self.sku.dict()

        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
