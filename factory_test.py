
from supplier import Supplier
from product_factory import ProductFactory


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies", "contact@example.com")

    physical = ProductFactory.create(
        "physical", "P001", "Laptop", 1200.00, 15, supplier, weight=2.5
    )

    digital = ProductFactory.create(
        "digital", "D001", "Photo Editor", 49.90, 100, supplier,
        download_size=850
    )

    print("Physical product:")
    physical.display_information()

    print("\nDigital product:")
    digital.display_information()

    print("\nTesting unknown product type:")

    try:
        ProductFactory.create(
            "service", "S002", "Installation", 30.00, 5, supplier
        )
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
