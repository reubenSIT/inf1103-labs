
import csv
import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout

from supplier import Supplier
from inventory import Inventory
from csv_loader import load_products


class TestCSVLoader(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )
        self.inventory = Inventory("Test Inventory")

    def create_csv(self, rows):
        file = tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            suffix=".csv",
            delete=False,
            encoding="utf-8"
        )

        with file:
            writer = csv.writer(file)
            writer.writerow([
                "product_type", "product_id", "name",
                "price", "stock_quantity"
            ])
            writer.writerows(rows)

        self.addCleanup(os.remove, file.name)
        return file.name

    def test_valid_products_load(self):
        path = self.create_csv([
            ["physical", "P001", "Desk Lamp", "25.00", "10"],
            ["digital", "D001", "Photo Editor", "49.90", "100"]
        ])

        output = io.StringIO()

        with redirect_stdout(output):
            load_products(path, self.inventory, self.supplier)

        self.assertEqual(len(self.inventory.products), 2)
        self.assertIn("2 products loaded.", output.getvalue())

    def test_invalid_rows_are_skipped(self):
        path = self.create_csv([
            ["physical", "P001", "Desk Lamp", "25.00", "10"],
            ["service", "S001", "Installation", "30.00", "5"],
            ["physical", "P002", "Office Chair", "abc", "3"],
            ["digital", "D001", "Photo Editor", "49.90", "100"]
        ])

        output = io.StringIO()

        with redirect_stdout(output):
            load_products(path, self.inventory, self.supplier)

        result = output.getvalue()

        self.assertEqual(len(self.inventory.products), 2)
        self.assertIn("Unknown product type", result)
        self.assertIn("could not convert string to float", result)
        self.assertIn("2 products loaded.", result)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "missing.csv")
            output = io.StringIO()

            with redirect_stdout(output):
                load_products(path, self.inventory, self.supplier)

            result = output.getvalue()

            self.assertIn("Products file not found:", result)
            self.assertIn("Load attempt finished.", result)
            self.assertEqual(len(self.inventory.products), 0)


if __name__ == "__main__":
    unittest.main()
