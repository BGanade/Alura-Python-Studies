# Program to calculate total activity duration

activity_a_duration = int(
    input("Enter the duration of activity A (in days): "))
activity_b_duration = int(
    input("Enter the duration of activity B (in days): "))
activity_c_duration = int(
    input("Enter the duration of activity C (in days): "))

total_duration = activity_a_duration + activity_b_duration + activity_c_duration

if (activity_a_duration < 0 or activity_b_duration < 0 or activity_c_duration < 0):
    print("Error: Durations cannot be negative.")
else:
    print(
        f"The total days needed to complete the activities are: {total_duration} days.")
