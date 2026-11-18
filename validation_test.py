
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies", "contact@example.com")

    physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)
    digital = DigitalProduct("D001", "Software", 50.00, 10, 250, supplier)

    try:
        PhysicalProduct("P002", "Mouse", -10.00, 5, 0.2, supplier)
    except ValueError as error:
        print("Invalid price:", error)

    try:
        DigitalProduct("D002", "Game", 20.00, -5, 500, supplier)
    except ValueError as error:
        print("Invalid stock:", error)

    try:
        OrderLine(physical, 0)
    except ValueError as error:
        print("Invalid quantity:", error)

    try:
        physical.update_stock(-3)
    except ValueError as error:
        print("Physical product:", error)

    try:
        digital.update_stock(-3)
    except ValueError as error:
        print("Digital product:", error)

    print("\nValid products:")
    physical.display_information()
    digital.display_information()


if __name__ == "__main__":
    main()
