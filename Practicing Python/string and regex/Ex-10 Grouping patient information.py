import re  # Import the regular expression module

# Get the patient's full name and year of birth from the user
data = input("Enter the patient's full name and year of birth: ")

# Define the regular expression pattern to capture parts of the data:
# (\w+)    - Group 1: Captures one or more word characters (for the first name)
# (\w+)    - Group 2: Captures one or more word characters (for the last name/surname)
# -        - Matches a literal hyphen
# (\d{4})  - Group 3: Captures exactly four digits (for the birth year)
pattern = r'(\w+) (\w+) - (\d{4})'

# Search for the pattern in the input data
result = re.search(pattern, data)

# Check if a match was found
if result:
    # Extract captured groups:
    # .group(1) gets the content of the first ()
    # .group(2) gets the content of the second ()
    # .group(3) gets the content of the third ()
    first_name = result.group(1)
    last_name = result.group(2)
    birth_year = result.group(3)

    # Print the extracted information
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Birth Year: {birth_year}")
else:
    # If no match is found, print an invalid format message
    print("Invalid format!")
