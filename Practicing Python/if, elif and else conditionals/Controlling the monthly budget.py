# Monthly Expense Tracker

budget_limit = 3000
monthly_expenses = float(input("Enter your total monthly expenses (R$): "))

if monthly_expenses > budget_limit:
    print("You've spent more than the stipulated limit.")
else:
    print("You are within the budget :-)")
