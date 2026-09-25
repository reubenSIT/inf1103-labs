failed_entries = 0
deliveries_processed = 0
transaction_history = []

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline())
            return inventory

    except FileNotFoundError:
        return 0

def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")
        file.write(",".join(map(str, history)))

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

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10  #10%

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = load_inventory()

# old w2lab + new stuff
while True:
    stock = get_valid_input()

    if stock == "quit":
        save_inventory(inventory, transaction_history)
        generate_report(deliveries_processed,failed_entries)
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)
    deliveries_processed += 1
    transaction_history.append(stock)
    # print("Transaction History:", transaction_history)  # to see transaction history in list

    tax = calculate_tax(stock)

    print("Inventory:", inventory)
    print("Tax for this delivery:", tax)

    if inventory > 500:
        print("Alert: Inventory exceeds 500 units")
        break


    