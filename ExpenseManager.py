expenseList =  []

def addExpense(expense):
    expenseList.append(expense)
    
def showAllExpenses():
    for expense in expenseList:
        print(expense.amount, expense.category, expense.description, expense.date)

def showTotalSum():
    totalSum = 0
    for expense in expenseList:
        totalSum += expense.amount

    print(totalSum)
