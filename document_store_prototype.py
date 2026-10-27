"""Tiny JSON document-style prototype using fictional product data."""
import json
from pathlib import Path


def main():
    products = [
        {"id": 1, "name": "Notebook", "category": "Stationery", "price": 45.0},
        {"id": 2, "name": "Pen", "category": "Stationery", "price": 10.0},
        {"id": 3, "name": "Mouse", "category": "Electronics", "price": 450.0},
    ]

    output_file = Path("products.json")
    output_file.write_text(json.dumps(products, indent=2), encoding="utf-8")
    documents = json.loads(output_file.read_text(encoding="utf-8"))

    print("Stationery products:")
    for item in documents:
        if item["category"] == "Stationery":
            print(item["name"], item["price"])


if __name__ == "__main__":
    main()
