
import unittest

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop",
            1200.00, 15, self.supplier, weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.get_product_id(), "P001")
        self.assertEqual(product.get_price(), 1200.00)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Software",
            50.00, 10, self.supplier, download_size=250
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertIsInstance(product, Product)
        self.assertEqual(product.get_product_id(), "D001")

    def test_unknown_product_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type"):
            ProductFactory.create(
                "service", "S002", "Installation",
                30.00, 5, self.supplier
            )

    def test_missing_physical_weight(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Mouse",
                20.00, 5, self.supplier
            )

    def test_missing_digital_download_size(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "D002", "Game",
                40.00, 10, self.supplier
            )


if __name__ == "__main__":
    unittest.main()
