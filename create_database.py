# create_database.py

import sqlite3

def create_database():
    conn = sqlite3.connect('budgetplanner.db')
    cursor = conn.cursor()

    # Create categories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    # Create expenses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT,
            amount INTEGER,
            category_id INTEGER,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == "__main__":
    create_database()

