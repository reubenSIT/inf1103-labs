
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


if __name__ == "__main__":
    main()
