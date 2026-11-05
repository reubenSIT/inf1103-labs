from abc import ABC, abstractmethod


# Abstract parent class
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# Interface-style abstract base class
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# PhysicalProduct inherits Product
# and implements the CanBeShipped interface
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        base_cost = 5.00
        cost_per_kg = 2.00

        shipping_cost = base_cost + (self.__weight * cost_per_kg)

        return shipping_cost


# DigitalProduct inherits Product only
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size:", self.__download_size, "MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."


# Temporary testing

print("=== PHYSICAL PRODUCT ===")

physical = PhysicalProduct(
    "P001", "Laptop", 1200.00, 15, 2.5
)

physical.display_information()

print("\n=== DIGITAL PRODUCT ===")

digital = DigitalProduct(
    "D001", "Photo Editor", 49.90, 100, 850
)

digital.display_information()


# Test fulfilment methods

print("\n=== FULFILMENT INFORMATION ===")

print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())


# Test shipping costs with different weights

print("\n=== SHIPPING COST TEST ===")

laptop = PhysicalProduct(
    "P002", "Laptop", 1200.00, 15, 2.5
)

mouse = PhysicalProduct(
    "P003", "Mouse", 25.50, 40, 0.2
)

print(f"Laptop shipping: ${laptop.calculate_shipping_cost():.2f}")
print(f"Mouse shipping: ${mouse.calculate_shipping_cost():.2f}")


# Test interface implementation

print("\n=== INTERFACE TEST ===")

print("PhysicalProduct can be shipped:",
      isinstance(physical, CanBeShipped))

print("DigitalProduct can be shipped:",
      isinstance(digital, CanBeShipped))


# Test abstract class

print("\n=== ABSTRACT CLASS TEST ===")

try:
    product = Product("P999", "Generic Product", 10.00, 5)

except TypeError as error:
    print("Expected error:", error)