# Program to calculate toll fee

# Input for distance
distance = float(input("Enter the distance traveled (in km): "))

# Toll fee calculation
if distance <= 100:
    toll_fee = 10.00
elif distance <= 200:
    toll_fee = 20.00
else:
    toll_fee = 30.00

# Output of the result
print(f"For {distance} km, the toll fee is: R$ {toll_fee:.2f}")
