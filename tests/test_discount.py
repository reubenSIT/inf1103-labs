
import unittest

from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)
from order import Order
from supplier import Supplier
from product_factory import ProductFactory


class TestDiscountStrategy(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)

    def test_bulk_below_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(150), 150)

    def test_student_discount(self):
        self.assertEqual(StudentDiscount().apply(250), 237.50)

    def test_order_strategy_change(self):
        supplier = Supplier("S001", "Test", "test@example.com")
        product = ProductFactory.create(
            "digital", "D001", "Software", 50.00, 10,
            supplier, download_size=100
        )

        order = Order("O001")
        order.add_order_line(product, 5)

        self.assertEqual(order.calculate_total(), 250)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)


if __name__ == "__main__":
    unittest.main()
