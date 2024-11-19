import sqlite3

DB_NAME = "products.db"


def initiate_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    """)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
            INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
        """, [
            ("Product1", "Ножи ручной работы", 100),
            ("Product2", "Охотничий нож GIKO", 200),
            ("Product3", "Нож керамбит", 300),
            ("Product4", "Нож Катран", 400),
        ])
        conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products

def add_test_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    """, [
        ("Product1", "Ножи ручной работы", 100),
        ("Product2", "Охотничий нож GIKO", 200),
        ("Product3", "Нож керамбит", 300),
        ("Product4", "Нож Катран", 400),
    ])
    conn.commit()
    conn.close()

    add_test_data()
    print("Тестовые данные успешно добавлены.")