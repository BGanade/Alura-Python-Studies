import re  # Import the regular expression module

# Get the client's name for validation
name = input("Enter the client's name for validation: ")

# Validate the name using a regular expression:
# - ^ (start of string)
# - [A-Z] (first letter must be an uppercase letter)
# - [a-z]* (followed by zero or more lowercase letters)
# - $ (end of string)
if re.fullmatch(r'[A-Z][a-z]*', name):
    print("Valid name!")
else:
    print("Invalid name!")
