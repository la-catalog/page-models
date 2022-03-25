import unittest
from unittest import TestCase
from datetime import datetime
from bson.objectid import ObjectId

from page_product import Product, Price, Attribute, Measurement, Rating, Metadata


class TestProduct(TestCase):
    def test_create_product_from_objects(self) -> None:
        Product(
            sku="3616585721",
            name="Smartphone Motorola Edge 20 128GB 5G Wi-Fi Tela 6,7'' Dual Chip 8GB RAM Câmera Tripla + Selfie 32MP - Branco",
            brand="MOTOROLA",
            description="O mais avançado e potente",
            gtin="7892597351206",
            prices=[Price(amount=2699, currency="R$")],
            segments=[
                "celulares e smartphones",
                "smartphone",
                "motorola",
                "motorola edge 20",
            ],
            attributes=[
                Attribute(name="Código", value="3616585721"),
                Attribute(name="Código de barras", value="7892597351206"),
                Attribute(name="Marca", value="MOTOROLA"),
                Attribute(name="Tipo de Chip", value="Nano Chip"),
                Attribute(name="Sistema Operacional", value="Android"),
                Attribute(name="Tipo de Tela", value="POLED"),
            ],
            measurement=Measurement(
                width=7.6,
                height=16.3,
                length=0.7,
                unit="cm",
                weight=163,
                weight_unit="g",
            ),
            rating=Rating(current=4.2, min=1, max=5),
            images=[],
            url="https://www.americanas.com.br/produto/3616585721",
            marketplace="americanas",
            metadata=Metadata(created=datetime.utcnow()),
        )

    def test_create_product_from_dict(self) -> None:
        Product(
            **{
                "sku": "3616585721",
                "name": "Smartphone Motorola Edge 20 128GB 5G Wi-Fi Tela 6,7'' Dual Chip 8GB RAM Câmera Tripla + Selfie 32MP - Branco",
                "brand": "MOTOROLA",
                "description": "O mais avançado e potente",
                "gtin": "7892597351206",
                "prices": [{"amount": 2699, "currency": "R$"}],
                "segments": [
                    "celulares e smartphones",
                    "smartphone",
                    "motorola",
                    "motorola edge 20",
                ],
                "attributes": [
                    {"name": "Código", "value": "3616585721"},
                    {"name": "Código de barras", "value": "7892597351206"},
                    {"name": "Marca", "value": "MOTOROLA"},
                    {"name": "Tipo de Chip", "value": "Nano Chip"},
                    {"name": "Sistema Operacional", "value": "Android"},
                    {"name": "Tipo de Tela", "value": "POLED"},
                ],
                "measurement": {
                    "width": 7.6,
                    "height": 16.3,
                    "length": 0.7,
                    "unit": "cm",
                    "weight": 163,
                    "weight_unit": "g",
                },
                "rating": {
                    "current": 4.2,
                    "min": 1,
                    "max": 5,
                },
                "images": [],
                "url": "https://www.americanas.com.br/produto/3616585721",
                "marketplace": "americanas",
                "metadata": {
                    "created": datetime.utcnow(),
                },
            }
        )

    def test_create_product_from_hybrid(self) -> None:
        Product(
            sku="3616585721",
            name="Smartphone Motorola Edge 20 128GB 5G Wi-Fi Tela 6,7'' Dual Chip 8GB RAM Câmera Tripla + Selfie 32MP - Branco",
            brand="MOTOROLA",
            description="O mais avançado e potente",
            gtin="7892597351206",
            prices=[{"amount": 2699, "currency": "R$"}],
            segments=[
                "celulares e smartphones",
                "smartphone",
                "motorola",
                "motorola edge 20",
            ],
            attributes=[
                {"name": "Código", "value": "3616585721"},
                {"name": "Código de barras", "value": "7892597351206"},
                {"name": "Marca", "value": "MOTOROLA"},
                {"name": "Tipo de Chip", "value": "Nano Chip"},
                {"name": "Sistema Operacional", "value": "Android"},
                {"name": "Tipo de Tela", "value": "POLED"},
            ],
            measurement={
                "width": 7.6,
                "height": 16.3,
                "length": 0.7,
                "unit": "cm",
                "weight": 163,
                "weight_unit": "g",
            },
            rating={
                "current": 4.2,
                "min": 1,
                "max": 5,
            },
            images=[],
            url="https://www.americanas.com.br/produto/3616585721",
            marketplace="americanas",
            metadata={
                "created": datetime.utcnow(),
            },
        )


if __name__ == "__main__":
    unittest.main()
