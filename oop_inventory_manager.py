class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)


# Temporary test
product1 = Product("P001", "Laptop", 1200.00, 15)

product1.display_information()

print("\nUpdating stock...\n")

product1.update_stock(20)
product1.display_information()