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


# Temporary testing

inventory = Inventory()

product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)
product3 = Product("P003", "Keyboard", 45.00, 25)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

inventory.display_all()

print("\nSearching for P002...\n")

found_product = inventory.search_product("P002")

if found_product is not None:
    found_product.display_information()

    print("\nUpdating P002 stock to 50...\n")
    found_product.update_stock(50)
    found_product.display_information()
else:
    print("Product not found.")