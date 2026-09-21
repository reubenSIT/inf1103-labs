inventory = 0     # initialize inventory to zero
failed_entries = 0

def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
        return "quit"

    if stock.startswith("-") and stock[1:].isdigit():
        print("Negative stock quantities are not allowed.")
        return None

    if not stock.isdigit():
        print("Invalid input. Please enter a number.")
        return None

    return int(stock)


while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
       print("Total Units Processed:", inventory)
       print("Number of Failed/Rejected Entries:", failed_entries)
       break

    if stock.startswith("-") and stock[1:].isdigit():
        print("Negative stock quantities are not allowed.")
        failed_entries += 1
        continue

    if not stock.isdigit():
        print("Invalid input. Please enter a number.")
        failed_entries += 1
        continue

    stock = int(stock)
    inventory += stock
    print("Inventory:", inventory)

    if inventory > 500:
        print("Alert: Inventory exceeds 500 units")
        break


    