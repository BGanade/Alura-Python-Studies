# Loan Application Check

# Data input
income = float(input("Enter your monthly income: "))
installment_value = float(input("Enter the desired installment value: "))

installment_limit = income * 0.3

# Verification
if income >= 2000 and installment_limit >= installment_value:
    print("Loan approved.")
elif income < 2000:
    print("Loan denied: Insufficient income.")
else:
    print(
        f"Loan denied: The installment value of ${installment_value:.2f} is greater than 30% of your monthly income of ${income:.2f}")
