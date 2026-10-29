import json


class Product:
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
        print("Current Inventory")
        print("--------------------------------")

        for product in self.__products:
            product.display_information()
            print("--------------------------------")

    def to_list(self):
        return [
            product.to_dict()
            for product in self.__products
        ]


# File handling functions

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

    return inventory


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved successfully to inventory.json.")


# Main program

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
        print("Add New Product")

        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        new_product = Product(
            product_id, name, price, stock
        )

        inventory.add_product(new_product)

        print("Product added successfully!")

    elif option == "3":
        print("Update Stock")

        product_id = input("Enter Product ID: ")
        found_product = inventory.search_product(product_id)

        if found_product is not None:
            print("Product Found:")
            found_product.display_information()

            new_stock = int(input("New Stock Quantity: "))
            found_product.update_stock(new_stock)

            print("Stock updated successfully!")
        else:
            print("Product not found.")

    elif option == "4":
        print("Search Product")

        product_id = input("Enter Product ID: ")
        found_product = inventory.search_product(product_id)

        if found_product is not None:
            print("Product Found:")
            found_product.display_information()
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