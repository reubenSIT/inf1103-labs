from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product


def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies Pte Ltd",
                        "contact@techsupplies.example")

    physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)
    digital = DigitalProduct("D001", "Photo Editor", 49.90, 100, 850, supplier)

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    print("\nDeleting supplier variable...")
    del supplier

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    inventory_a = Inventory("Inventory A")
    inventory_b = Inventory("Inventory B")

    print("\nProduct before adding to inventory:")
    physical.display_information()

    inventory_a.add_product(physical)
    inventory_a.add_product(digital)

    inventory_a.display_all_products()

    print("\nSearching for P001...")
    found = inventory_a.find_product("P001")

    if found is not None:
        found.display_information()

    print("\nRemoving P001 from Inventory A...")
    removed_product = inventory_a.remove_product("P001")

    inventory_a.display_all_products()

    if removed_product is not None:
        print("\nProduct after removal:")
        removed_product.display_information()

        inventory_b.add_product(removed_product)
        inventory_b.display_all_products()

        transferred_product = inventory_b.find_product("P001")
        print("\nSame product object:", transferred_product is physical)

    print("\nFinal inventories:")
    inventory_a.display_all_products()
    inventory_b.display_all_products()

    order1 = Order("O001")
    order2 = Order("O002")

    order1.add_order_line(physical, 1)
    order1.add_order_line(digital, 2)
    order2.add_order_line(physical, 2)

    print("\nOrders created:")
    order1.display_order()
    order2.display_order()

    print("\nComparing order objects:")
    print("Same OrderLine:", order1.order_lines[0] is order2.order_lines[0])
    print("Same Product:", order1.order_lines[0].product is order2.order_lines[0].product)

    print("\nRemoving laptop from O001...")
    order1.remove_order_line("P001")

    order1.display_order()
    order2.display_order()

    print("\nLaptop still exists:")
    physical.display_information()

    print("\nProduct details:")
    show_product_details(physical)
    show_product_details(digital)

    print("\nUpdating stock:")
    physical.update_stock(14)
    digital.update_stock(99)

    physical.display_information()
    digital.display_information()

    inventory_a.remove_product("D001")
    inventory_b.remove_product("P001")

    mixed_inventory = Inventory("Mixed Inventory")
    mixed_inventory.add_product(physical)
    mixed_inventory.add_product(digital)

    print("\nProducts in mixed inventory:")
    for product in mixed_inventory.products:
        show_product_details(product)
        print("--------------------------------")

    print("\nChecking previous inventories:")
    inventory_a.display_all_products()
    inventory_b.display_all_products()


if __name__ == "__main__":
    main()

from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from order import Order
from product import Product


def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())


def main() -> None:
    supplier = Supplier("S001", "Tech Supplies Pte Ltd",
                        "contact@techsupplies.example")

    physical = ProductFactory.create(
        "physical", "P001", "Laptop", 1200.00, 15, supplier,
        weight=2.5
    )

    digital = ProductFactory.create(
        "digital", "D001", "Photo Editor", 49.90, 100, supplier,
        download_size=850
    )

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    print("\nDeleting supplier variable...")
    del supplier

    print("\nPhysical product supplier:")
    physical.display_supplier_information()

    print("\nDigital product supplier:")
    digital.display_supplier_information()

    inventory_a = Inventory("Inventory A")
    inventory_b = Inventory("Inventory B")

    print("\nProduct before adding to inventory:")
    physical.display_information()

    inventory_a.add_product(physical)
    inventory_a.add_product(digital)

    inventory_a.display_all_products()

    print("\nSearching for P001...")
    found = inventory_a.find_product("P001")

    if found is not None:
        found.display_information()

    print("\nRemoving P001 from Inventory A...")
    removed_product = inventory_a.remove_product("P001")

    inventory_a.display_all_products()

    if removed_product is not None:
        print("\nProduct after removal:")
        removed_product.display_information()

        inventory_b.add_product(removed_product)
        inventory_b.display_all_products()

        transferred_product = inventory_b.find_product("P001")
        print("\nSame product object:", transferred_product is physical)

    print("\nFinal inventories:")
    inventory_a.display_all_products()
    inventory_b.display_all_products()

    order1 = Order("O001")
    order2 = Order("O002")

    order1.add_order_line(physical, 1)
    order1.add_order_line(digital, 2)
    order2.add_order_line(physical, 2)

    print("\nOrders created:")
    order1.display_order()
    order2.display_order()

    print("\nComparing order objects:")
    print("Same OrderLine:", order1.order_lines[0] is order2.order_lines[0])
    print("Same Product:", order1.order_lines[0].product is order2.order_lines[0].product)

    print("\nRemoving laptop from O001...")
    order1.remove_order_line("P001")

    order1.display_order()
    order2.display_order()

    print("\nLaptop still exists:")
    physical.display_information()

    print("\nProduct details:")
    show_product_details(physical)
    show_product_details(digital)

    print("\nUpdating stock:")
    physical.update_stock(14)
    digital.update_stock(99)

    physical.display_information()
    digital.display_information()

    inventory_a.remove_product("D001")
    inventory_b.remove_product("P001")

    mixed_inventory = Inventory("Mixed Inventory")
    mixed_inventory.add_product(physical)
    mixed_inventory.add_product(digital)

    print("\nProducts in mixed inventory:")
    for product in mixed_inventory.products:
        show_product_details(product)
        print("--------------------------------")

    print("\nChecking previous inventories:")
    inventory_a.display_all_products()
    inventory_b.display_all_products()


if __name__ == "__main__":
    main()
