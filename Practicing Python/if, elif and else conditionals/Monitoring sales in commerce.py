# Fruit Sales Comparison

apples_sold = int(input("Enter the quantity of apples sold: "))
bananas_sold = int(input("Enter the quantity of bananas sold: "))

if apples_sold > bananas_sold:
    print("Apples had higher sales.")
elif bananas_sold > apples_sold:
    print("Bananas had higher sales.")
else:
    print("Sales were equal.")
