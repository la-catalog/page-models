import unittest
from unittest import TestCase

from page_sku import SKU, Attribute, Measurement, Price, Rating


class TestCreateSKU(TestCase):
    def test_create_sku_from_objects(self) -> None:
        SKU(
            code="3616585721",
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
            images=[
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_1SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_2SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_3SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_4SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_5SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_6SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_7SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_8SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_9SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_10SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_11SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_12SZ.jpg",
            ],
            sources=["https://www.americanas.com.br/produto/3616585721"],
            marketplace="americanas",
        )

    def test_create_sku_from_dict(self) -> None:
        SKU(
            **{
                "code": "3616585721",
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
                "images": [
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_1SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_2SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_3SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_4SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_5SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_6SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_7SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_8SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_9SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_10SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_11SZ.jpg",
                    "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_12SZ.jpg",
                ],
                "sources": ["https://www.americanas.com.br/produto/3616585721"],
                "marketplace": "americanas",
            }
        )

    def test_create_sku_from_hybrid(self) -> None:
        SKU(
            code="3616585721",
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
            images=[
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_1SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_2SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_3SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_4SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_5SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_6SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_7SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_8SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_9SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_10SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_11SZ.jpg",
                "https://images-americanas.b2w.io/produtos/01/00/img/3616585/7/3616585730_12SZ.jpg",
            ],
            sources=["https://www.americanas.com.br/produto/3616585721"],
            marketplace="americanas",
        )


if __name__ == "__main__":
    unittest.main()
