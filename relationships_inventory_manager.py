
from abc import ABC, abstractmethod


# Supplier class
class Supplier:
    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        print("Supplier ID:", self.__supplier_id)
        print("Supplier Name:", self.__name)
        print("Contact Email:", self.__contact_email)


# Abstract Product class
class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock

        # Association: Product references an existing Supplier
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


# Interface-style abstract class
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass


# PhysicalProduct subclass
class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock, supplier
        )
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print("Type: Physical")
        print("Weight:", self.__weight, "kg")
        print(
            f"Shipping Cost: "
            f"${self.calculate_shipping_cost():.2f}"
        )

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5.00 + (self.__weight * 2.00)


# DigitalProduct subclass
class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier
    ) -> None:
        super().__init__(
            product_id, name, price, stock, supplier
        )
        self.__download_size: float = download_size

    def display_information(self) -> None:
        super().display_information()
        print("Type: Digital")
        print("Download Size:", self.__download_size, "MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."


# Phase 1: Association testing
def main() -> None:

    print("=== CREATE SUPPLIER ===")

    supplier = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "contact@techsupplies.example"
    )

    supplier.display_information()

    print("\n=== CREATE PRODUCTS ===")

    physical = PhysicalProduct(
        "P001",
        "Laptop",
        1200.00,
        15,
        2.5,
        supplier
    )

    digital = DigitalProduct(
        "D001",
        "Photo Editor",
        49.90,
        100,
        850,
        supplier
    )

    print("\n=== PHYSICAL PRODUCT ===")
    physical.display_information()

    print("\nSupplier Information:")
    physical.display_supplier_information()

    print("\n=== DIGITAL PRODUCT ===")
    digital.display_information()

    print("\nSupplier Information:")
    digital.display_supplier_information()

    # Predict First test
    print("\n=== ASSOCIATION TEST ===")

    print("Deleting the local supplier variable...")
    del supplier

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    print("\nAssociation test completed.")


if __name__ == "__main__":
    main()
