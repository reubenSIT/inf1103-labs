
from supplier import Supplier
from inventory import Inventory
from csv_loader import load_products


def main() -> None:
    supplier = Supplier(
        "S001", "Tech Supplies", "contact@example.com"
    )

    inventory = Inventory("CSV Inventory")

    print("=== Loading products.csv ===")
    load_products("products.csv", inventory, supplier)

    print("\n=== Loaded Products ===")
    inventory.display_all_products()

    print("\n=== Testing Missing File ===")
    load_products("missing_products.csv", inventory, supplier)


if __name__ == "__main__":
    main()
