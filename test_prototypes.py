import json
import sqlite3
import unittest


class PrototypeTests(unittest.TestCase):
    def setUp(self):
        self.products = [
            {"id": 1, "name": "Notebook", "category": "Stationery", "price": 45.0},
            {"id": 2, "name": "Pen", "category": "Stationery", "price": 10.0},
            {"id": 3, "name": "Mouse", "category": "Electronics", "price": 450.0},
        ]

    def test_sqlite_category_filter(self):
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE products (id INTEGER, name TEXT, category TEXT, price REAL)")
        cursor.executemany(
            "INSERT INTO products VALUES (?, ?, ?, ?)",
            [(p["id"], p["name"], p["category"], p["price"]) for p in self.products],
        )
        cursor.execute("SELECT name FROM products WHERE category = ?", ("Stationery",))
        self.assertEqual([row[0] for row in cursor.fetchall()], ["Notebook", "Pen"])
        connection.close()

    def test_json_document_category_filter(self):
        stationery = [p["name"] for p in self.products if p["category"] == "Stationery"]
        self.assertEqual(stationery, ["Notebook", "Pen"])
        self.assertEqual(json.loads(json.dumps(self.products)), self.products)


if __name__ == "__main__":
    unittest.main()
