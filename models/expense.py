import sqlite3

class Expense:
    conn = sqlite3.connect('budgetplanner.db')
    cursor = conn.cursor()

    @classmethod
    def create(cls, name, amount, category_id):
        cls.cursor.execute("INSERT INTO expenses (name, amount, category_id) VALUES (?, ?, ?)", (name, amount, category_id))
        cls.conn.commit()
        print("Expense added successfully.")

    @classmethod
    def delete(cls, expense_id):
        cls.cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        cls.conn.commit()
        print("Expense deleted successfully.")

    @classmethod
    def get_all(cls):
        cls.cursor.execute("SELECT * FROM expenses")
        expenses = cls.cursor.fetchall()
        return expenses

    @classmethod
    def find_by_id(cls, expense_id):
        cls.cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        expense = cls.cursor.fetchone()
        return expense


Expense.create('Groceries', 3000, 1)  # Expense name, amount, category_id
Expense.create('Fare', 6000, 2)
Expense.create('Movie tickets', 1000, 3)