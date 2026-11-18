
import csv

from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def load_products(path: str, inventory: Inventory,
                  supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Invalid number of columns")

                    product_type, product_id, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier,
                        weight=0.0,
                        download_size=0.0
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")
