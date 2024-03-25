import sys


class BudgetCLI:
    def __init__(self):
        self.categories = {}

    # Define your CLI functionality here
    def display_categories():
        categories = Category.get_all()
        print("Categories:")
        for category in categories:
            print(category)

    def display_expenses():
        expenses = Expense.get_all()
        print("Expenses:")
        for expense in expenses:
            print(expense)

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
        category_name = input("Enter category name: ")
        if category_name in self.categories:
            print("Category already exists.")
        else:
            self.categories[category_name] = []
            print(f"Category '{category_name}' added successfully.")

    def add_expense(self):
        category_name = input("Enter category name: ")
        if category_name not in self.categories:
            print("Error: Category not found.")
            return
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        self.categories[category_name].append((expense_name, expense_amount))
        print(f"Expense '{expense_name}' added to category '{category_name}'.")

    def delete_category(self):
        category_name = input("Enter category name to delete: ")
        if category_name in self.categories:
            del self.categories[category_name]
            print(f"Category '{category_name}' deleted successfully.")
        else:
            print("Error: Category not found.")

    def delete_expense(self):
        category_name = input("Enter category name: ")
        if category_name not in self.categories:
            print("Error: Category not found.")
            return
        expense_name = input("Enter expense name to delete: ")
        expenses = self.categories[category_name]
        for i, (name, _) in enumerate(expenses):
            if name == expense_name:
                del expenses[i]
                print(f"Expense '{expense_name}' deleted from category '{category_name}'.")
                return
        print(f"Error: Expense '{expense_name}' not found in category '{category_name}'.")

    def view_all_categories(self):
        print("Categories:")
        for category in self.categories:
            print("-", category)

    def view_all_expenses(self):
        print("Expenses:")
        for category, expenses in self.categories.items():
            print(f"Category: {category}")
            for expense_name, expense_amount in expenses:
                print(f"- {expense_name}: {expense_amount}")

    def find_expense_by_name(self):
        search_name = input("Enter expense name to search: ")
        found = False
        for category, expenses in self.categories.items():
            for expense_name, expense_amount in expenses:
                if expense_name == search_name:
                    found = True
                    print(f"Category: {category}, Expense: {expense_name}, Amount: {expense_amount}")
        if not found:
            print(f"No expense found with name '{search_name}'.")

if __name__ == "__main__":
    budget_cli = BudgetCLI()
    budget_cli.run()


from models.category import Category
from models.expense import Expense

