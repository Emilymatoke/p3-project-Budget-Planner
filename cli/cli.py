import sys
import sqlite3

class BudgetCLI:
    def __init__(self):
        self.conn = sqlite3.connect('budgetplanner.db')
        self.cursor = self.conn.cursor()

    def display_menu(self):
        print("Budget Planner Application")
        print("1. Add Category")
        print("2. Add Expense")
        print("3. Delete Category")
        print("4. Delete Expense")
        print("5. View All Categories")
        print("6. View All Expenses")
        print("7. Find Expense by Name")
        print("8. Exit")

    def run(self):
        self.create_database()  # Ensure the database is created
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_category()
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.delete_category()
            elif choice == '4':
                self.delete_expense()
            elif choice == '5':
                self.view_all_categories()
            elif choice == '6':
                self.view_all_expenses()
            elif choice == '7':
                self.find_expense_by_name()
            elif choice == '8':
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice, please try again.")

    def create_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                name TEXT,
                amount INTEGER,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        """)
        self.conn.commit()

    def add_category(self):
        category_name = input("Enter category name: ")
        self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
        self.conn.commit()
        print(f"Category '{category_name}' added successfully.")

    def add_expense(self):
        category_name = input("Enter category name: ")
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        self.cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
        category = self.cursor.fetchone()
        if category:
            category_id = category[0]
            self.cursor.execute("INSERT INTO expenses (name, amount, category_id) VALUES (?, ?, ?)", (expense_name, expense_amount, category_id))
            self.conn.commit()
            print(f"Expense '{expense_name}' added to category '{category_name}'.")
        else:
            print("Error: Category not found.")

    def delete_category(self):
        category_id = int(input("Enter category ID to delete: "))
        self.cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        self.conn.commit()
        print("Category deleted successfully.")

    def delete_expense(self):
        expense_id = int(input("Enter expense ID to delete: "))
        self.cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self.conn.commit()
        print("Expense deleted successfully.")

    def view_all_categories(self):
        self.cursor.execute("SELECT * FROM categories")
        categories = self.cursor.fetchall()
        print("Categories:")
        for category in categories:
            print("-", category[1])  # category[1] contains the category name

    def view_all_expenses(self):
        self.cursor.execute("SELECT expenses.name, expenses.amount, categories.name FROM expenses JOIN categories ON expenses.category_id = categories.id")
        expenses = self.cursor.fetchall()
        print("Expenses:")
        for expense in expenses:
            print(f"Category: {expense[2]}, Expense: {expense[0]}, Amount: {expense[1]}")

    def find_expense_by_name(self):
        search_name = input("Enter expense name to search: ")
        self.cursor.execute("SELECT expenses.name, expenses.amount, categories.name FROM expenses JOIN categories ON expenses.category_id = categories.id WHERE expenses.name = ?", (search_name,))
        found_expenses = self.cursor.fetchall()
        if found_expenses:
            print("Found expenses:")
            for expense in found_expenses:
                print(f"Category: {expense[2]}, Expense: {expense[0]}, Amount: {expense[1]}")
        else:
            print(f"No expense found with name '{search_name}'.")

if __name__ == "__main__":
    budget_cli = BudgetCLI()
    budget_cli.run()
