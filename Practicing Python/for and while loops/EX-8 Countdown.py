# Loop while time is greater than 0
for seconds in range(10, 0, -1):
    # Check if the current time is an even number
    if seconds % 2 == 0:
        # Print a specific message for even numbers
        print(f"Only {seconds} seconds left - Don't miss this opportunity!")
    else:
        # Print a different message for odd numbers
        print(f"The countdown continues: {seconds} seconds remaining.")
