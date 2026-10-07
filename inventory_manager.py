import json


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

        return []


inventory = load_inventory()


def display_all():
    print("Current Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("------------------------------------------------")


def add_product():
    print("Add New Product")

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")


def update_stock():
    print("Update Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product():
    print("Search Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return

    print("Product not found.")


display_all()

add_product()

display_all()

update_stock()

display_all()

search_product()