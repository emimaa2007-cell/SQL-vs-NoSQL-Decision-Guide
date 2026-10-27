"""Tiny SQL prototype using fictional product data."""
import sqlite3


def main():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    products = [
        (1, "Notebook", "Stationery", 45.0),
        (2, "Pen", "Stationery", 10.0),
        (3, "Mouse", "Electronics", 450.0),
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)

    print("Stationery products:")
    cursor.execute(
        "SELECT name, price FROM products WHERE category = ?",
        ("Stationery",),
    )
    for row in cursor.fetchall():
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
