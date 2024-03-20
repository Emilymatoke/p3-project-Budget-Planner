import sys

class BudgetCLI:
    def __init__(self):
        self.categories = []
        self.expenses = []

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

    def add_category(self):
        name = input("Enter category name: ")
        Category.create(name)
        print("Category added successfully.")

    def add_expense(self):
        name = input("Enter expense name: ")
        amount = int(input("Enter expense amount: "))
        category_id = int(input("Enter category ID: "))
        Expense.create(name, amount, category_id)
        print("Expense added successfully.")

    def delete_category(self):
        category_id = int(input("Enter category ID to delete: "))
        Category.delete(category_id)
        print("Category deleted successfully.")

    def delete_expense(self):
        expense_id = int(input("Enter expense ID to delete: "))
        Expense.delete(expense_id)
        print("Expense deleted successfully.")

    def view_all_categories(self):
        print("Categories:")
        categories = Category.get_all()
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[1]}")

    def view_all_expenses(self):
        print("Expenses:")
        expenses = Expense.get_all()
        for expense in expenses:
            print(f"ID: {expense[0]}, Name: {expense[1]}, Amount: {expense[2]}, Category ID: {expense[3]}")

    def find_expense_by_name(self):
        name = input("Enter expense name to search: ")
        expenses = Expense.find_by_name(name)
        if expenses:
            print("Expenses Found:")
            for expense in expenses:
                print(f"ID: {expense[0]}, Name: {expense[1]}, Amount: {expense[2]}, Category ID: {expense[3]}")
        else:
            print("No expenses found with the given name.")

if __name__ == "__main__":
    budget_cli = BudgetCLI()
    budget_cli.run()


from models.category import Category
from models.expense import Expense
1