
from abc import ABC, abstractmethod


class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        print("Supplier ID:", self.__supplier_id)
        print("Supplier Name:", self.__name)
        print("Contact Email:", self.__contact_email)


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_price(self) -> float:
        return self.__price

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self) -> None:
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print("Type: Physical")
        print("Weight:", self.__weight, "kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5.00 + (self.__weight * 2.00)


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print("Type: Digital")
        print("Download Size:", self.__download_size, "MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."


class Inventory:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def remove_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                return product
        return None

    def display_all_products(self) -> None:
        print(f"\n=== {self.__name} ===")

        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print("Fulfilment:", product.get_fulfilment_info())
            print("--------------------------------")


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

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
        return total

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


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies Pte Ltd",
                        "contact@techsupplies.example")

    physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)
    digital = DigitalProduct("D001", "Photo Editor", 49.90, 100, 850, supplier)

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    print("\nDeleting supplier variable...")
    del supplier

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    inventory_a = Inventory("Inventory A")
    inventory_b = Inventory("Inventory B")

    print("\nProduct before adding to inventory:")
    physical.display_information()

    inventory_a.add_product(physical)
    inventory_a.add_product(digital)

    inventory_a.display_all_products()

    print("\nSearching for P001...")
    found = inventory_a.find_product("P001")

    if found is not None:
        found.display_information()

    print("\nRemoving P001 from Inventory A...")
    removed_product = inventory_a.remove_product("P001")

    inventory_a.display_all_products()

    if removed_product is not None:
        print("\nProduct after removal:")
        removed_product.display_information()

        inventory_b.add_product(removed_product)
        inventory_b.display_all_products()

        transferred_product = inventory_b.find_product("P001")
        print("\nSame product object:", transferred_product is physical)

    print("\nFinal inventories:")
    inventory_a.display_all_products()
    inventory_b.display_all_products()

    order1 = Order("O001")
    order2 = Order("O002")

    order1.add_order_line(physical, 1)
    order1.add_order_line(digital, 2)

    order2.add_order_line(physical, 2)

    print("\nOrders created:")
    order1.display_order()
    order2.display_order()

    print("\nComparing order objects:")
    print("Same OrderLine:", order1.order_lines[0] is order2.order_lines[0])
    print("Same Product:", order1.order_lines[0].product is order2.order_lines[0].product)

    print("\nRemoving laptop from O001...")
    order1.remove_order_line("P001")

    order1.display_order()
    order2.display_order()

    print("\nLaptop still exists:")
    physical.display_information()


if __name__ == "__main__":
    main()
