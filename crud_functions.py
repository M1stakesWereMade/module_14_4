import sqlite3

def initiate_db():
    """Создает таблицу Products, если она еще не существует."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    """Возвращает все записи из таблицы Products."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def populate_products():
    """Заполняет таблицу Products тестовыми данными."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.executemany('''
        INSERT INTO Products (title, description, price)
        VALUES (?, ?, ?)
    ''', [
        ('Продукт 1', 'Описание 1', 100),
        ('Продукт 2', 'Описание 2', 200),
        ('Продукт 3', 'Описание 3', 300),
        ('Продукт 4', 'Описание 4', 400),
    ])
    connection.commit()
    connection.close()
