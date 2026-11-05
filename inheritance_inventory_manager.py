from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."


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
physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
physical.display_information()

print("\n=== DIGITAL PRODUCT ===")
digital = DigitalProduct("D001", "Photo Editor", 49.90, 100, 850)
digital.display_information()

print("\n=== FULFILMENT INFORMATION ===")
print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())


print("\n=== ABSTRACT CLASS TEST ===")

try:
    product = Product("P999", "Generic Product", 10.0, 5)
except TypeError as error:
    print("Expected error:", error)