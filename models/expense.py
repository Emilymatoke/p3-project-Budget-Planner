import sqlite3

DATABASE_FILE = "budgetplanner.db"

class Expense:
    @classmethod
    def create(cls, name, amount, category_id):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (name, amount, category_id) VALUES (?, ?, ?)", (name, amount, category_id))
        conn.commit()
        conn.close()
        print("Expense added successfully.")

    @classmethod
    def delete(cls, expense_id):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        conn.close()
        return expenses

    @classmethod
    def find_by_id(cls, expense_id):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        expense = cursor.fetchone()
        conn.close()
        return expense