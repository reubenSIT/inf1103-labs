from product import Product


class Inventory:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def remove_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)
                return product
        return None

    def display_all_products(self) -> None:
        print(f"\n=== {self.__name} ===")

        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display_information()
            print("Fulfilment:", product.get_fulfilment_info())
            print("--------------------------------")
