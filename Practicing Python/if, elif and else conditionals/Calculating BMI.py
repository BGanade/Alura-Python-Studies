# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)
print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Classification: Underweight")
elif 18.5 <= bmi < 25:
    print("Classification: Normal weight")
elif 25 <= bmi < 30:
    print("Classification: Overweight")
elif 30 <= bmi < 35:
    print("Classification: Obesity class 1")
elif 35 <= bmi < 40:
    print("Classification: Obesity class 2")
else:
    print("Classification: Obesity class 3 (Morbid obesity)")
