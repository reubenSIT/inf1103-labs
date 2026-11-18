
from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount


class Order:
    def __init__(self, order_id: str,
                 discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        line = OrderLine(product, quantity)
        self.order_lines.append(line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.order_lines:
            if line.product.get_product_id() == product_id:
                self.order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.order_lines:
            total += line.calculate_subtotal()
        return self.discount.apply(total)

    def display_order(self) -> None:
        print(f"\nOrder: {self.order_id}")

        if not self.order_lines:
            print("No items in order.")
            return

        for line in self.order_lines:
            print("Product:", line.product.get_product_id())
            print("Quantity:", line.quantity)
            print(f"Subtotal: ${line.calculate_subtotal():.2f}")

        print(f"Total: ${self.calculate_total():.2f}")
