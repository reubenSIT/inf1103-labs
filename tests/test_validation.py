
import unittest

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

        self.physical = PhysicalProduct(
            "P001", "Laptop", 1200.00, 15, 2.5, self.supplier
        )

        self.digital = DigitalProduct(
            "D001", "Software", 50.00, 10, 250, self.supplier
        )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Mouse", -10.00, 5, 0.2, self.supplier
            )

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            DigitalProduct(
                "D002", "Game", 0, 10, 500, self.supplier
            )

    def test_negative_initial_stock(self):
        with self.assertRaises(ValueError):
            DigitalProduct(
                "D003", "Game", 20.00, -5, 500, self.supplier
            )

    def test_zero_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.physical, 0)

    def test_negative_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.physical, -2)

    def test_negative_physical_stock_update(self):
        with self.assertRaises(ValueError):
            self.physical.update_stock(-3)

    def test_negative_digital_stock_update(self):
        with self.assertRaises(ValueError):
            self.digital.update_stock(-3)

    def test_valid_stock_update(self):
        self.physical.update_stock(20)
        self.digital.update_stock(5)

        self.assertEqual(self.physical.get_product_id(), "P001")
        self.assertEqual(self.digital.get_product_id(), "D001")


if __name__ == "__main__":
    unittest.main()
