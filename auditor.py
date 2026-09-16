inventory = 0     # initialize inventory to zero

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
       break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Negative stock quantities are not allowed.")
        continue

    if not stock.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    stock = int(stock)
    inventory += stock
    print("Inventory:", inventory)

    if inventory > 500:
        print("Alert: Inventory exceeds 500 units")
        break


    