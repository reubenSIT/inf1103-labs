
import json
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

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# Interface-style abstract base class
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# Physical product subclass
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Type: Physical")
        print("Weight:", self.__weight, "kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        base_cost = 5.00
        cost_per_kg = 2.00
        return base_cost + (self.__weight * cost_per_kg)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


# Digital product subclass
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print("Type: Digital")
        print("Download Size:", self.__download_size, "MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


# Inventory manages a collection of products
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("--------------------------------")

        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print("Fulfilment:", product.get_fulfilment_info())
            print("--------------------------------")

    def to_list(self):
        return [product.to_dict() for product in self.__products]


# Load inventory data from JSON
def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product_type = item.get("type", "physical")

            if product_type == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item.get("weight", 0.0)
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                print("Unknown product type:", product_type)
                continue

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print("Error loading inventory:", error)
        print("Starting with an empty inventory.")
        inventory = Inventory()

    return inventory


# Save inventory data to JSON
def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# Helper function for numeric input
def get_non_negative_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Invalid number. Please try again.")


# Main program
def main():
    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("\nAdd New Product")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Select product type: ")

            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

            product_id = input("Product ID: ")

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            name = input("Product Name: ")
            price = get_non_negative_number("Price: ", float)
            stock = get_non_negative_number("Stock Quantity: ", int)

            if product_type == "1":
                weight = get_non_negative_number(
                    "Weight (kg): ", float
                )

                new_product = PhysicalProduct(
                    product_id, name, price, stock, weight
                )

            else:
                download_size = get_non_negative_number(
                    "Download Size (MB): ", float
                )

                new_product = DigitalProduct(
                    product_id, name, price, stock, download_size
                )

            inventory.add_product(new_product)
            print("Product added successfully!")

        elif option == "3":
            print("\nUpdate Stock")
            product_id = input("Enter Product ID: ")

            found_product = inventory.search_product(product_id)

            if found_product is not None:
                print("Product Found:")
                found_product.display_information()

                new_stock = get_non_negative_number(
                    "New Stock Quantity: ", int
                )

                found_product.update_stock(new_stock)
                print("Stock updated successfully!")

            else:
                print("Product not found.")

        elif option == "4":
            print("\nSearch Product")
            product_id = input("Enter Product ID: ")

            found_product = inventory.search_product(product_id)

            if found_product is not None:
                print("Product Found:")
                found_product.display_information()
                print(
                    "Fulfilment:",
                    found_product.get_fulfilment_info()
                )

            else:
                print("Product not found.")

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
