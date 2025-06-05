# Initialize an empty list to store volunteer names
volunteers = []

# Start an infinite loop to collect names
while True:
    # Prompt the user for a volunteer's name or the exit command
    name = input("Enter the volunteer's name (or 'exit' to finish): ")

    # Check if the user entered the exit command (case-insensitive)
    if name.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    # Add the entered name to the list of volunteers
    volunteers.append(name)

# Print the list of registered volunteers after the loop ends
print("\nRegistered volunteers:", volunteers)
