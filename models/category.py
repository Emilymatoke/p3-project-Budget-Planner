import sqlite3

class Category:
    conn = sqlite3.connect('budgetplanner.db')
    cursor = conn.cursor()

    @classmethod
    def create(cls, name):
        cls.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        cls.conn.commit()
        print("Category added successfully.")

    @classmethod
    def delete(cls, category_id):
        cls.cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        cls.conn.commit()
        print("Category deleted successfully.")

    @classmethod
    def get_all(cls):
        cls.cursor.execute("SELECT * FROM categories")
        categories = cls.cursor.fetchall()
        return categories

    @classmethod
    def find_by_id(cls, category_id):
        cls.cursor.execute("SELECT * FROM categories WHERE id = ?", (category_id,))
        category = cls.cursor.fetchone()
        return category


# Create categories
Category.create('Food')
Category.create('Transportation')
Category.create('Entertainment')