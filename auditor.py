inventory = 0     # initialize inventory to zero

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
       break

    if not stock.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    stock = int(stock)

    