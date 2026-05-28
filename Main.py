from Expense import Expense
from ExpenseManager import ExpenseManager

manager = ExpenseManager()

while choice != 4:
    print("[1] Add expense")
    print("[2] Show all expenses")
    print("[3] Show total sum")
    print("[4] Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date: ")

        expense = Expense(amount, category, description, date)
        manager.addExpense(expense)