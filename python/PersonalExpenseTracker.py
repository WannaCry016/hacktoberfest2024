import datetime
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, amount, category, description=""):
        expense = {
            'date': str(datetime.date.today()),
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        print("Expense added!")

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)
    
    def save_to_file(self, filename="expenses.json"):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)
        print(f"Expenses saved to {filename}!")

# Example usage
tracker = ExpenseTracker()
tracker.add_expense(10, "Food", "Lunch")
tracker.add_expense(25, "Transport", "Taxi")
tracker.view_expenses()
tracker.save_to_file()
