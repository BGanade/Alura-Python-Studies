# Stock management system

stock = 5
# Loop while stock is greater than 0
while stock > 0:
    # Print a message indicating a sale and the remaining stock
    print(f"Sale made! Remaining stock: {stock}")
    # Decrease stock by 1 after each sale
    stock -= 1
# Print a message indicating that the stock is depleted after the loop finishes
print("Stock depleted.")
