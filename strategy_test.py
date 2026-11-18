
from supplier import Supplier
from digital_product import DigitalProduct
from order import Order
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies", "contact@example.com")
    product = DigitalProduct("D001", "Software", 50.00, 10, 250.0, supplier)

    order = Order("O001", NoDiscount())
    order.add_order_line(product, 5)

    print(f"Original total: ${order.calculate_total():.2f}")

    order.set_discount(BulkDiscount(200, 20))
    print(f"Bulk discount total: ${order.calculate_total():.2f}")

    order.set_discount(PercentageDiscount(10))
    print(f"Percentage discount total: ${order.calculate_total():.2f}")


if __name__ == "__main__":
    main()
