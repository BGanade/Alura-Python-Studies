# Student Grade Calculator

grade1 = float(input("Enter the student's first grade: "))
grade2 = float(input("Enter the student's second grade: "))
grade3 = float(input("Enter the student's third grade: "))

average = (grade1 + grade2 + grade3) / 3

print(f"The average grade is {average:.2f}")

if average < 5:
    print("Status: Failed")
elif 5 <= average < 7:
    print("Status: Recovery")
else:
    print("Status: Approved")
