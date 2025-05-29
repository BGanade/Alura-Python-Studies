import re  # Import the regular expression module

# Get the CPF from the user in the specified format
cpf = input("Enter the CPF in XXX.XXX.XXX-XX format: ")

# Define the regular expression pattern for CPF validation:
# \d{3}  - Matches exactly 3 digits
# \.     - Matches a literal dot (escaped with \)
# \d{3}  - Matches exactly 3 digits
# \.     - Matches a literal dot
# \d{3}  - Matches exactly 3 digits
# -      - Matches a literal hyphen
# \d{2}  - Matches exactly 2 digits
pattern = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

# Search for the pattern anywhere within the input CPF string
if re.search(pattern, cpf):
    print("The CPF format is correct.")
else:
    print("The CPF format is incorrect.")
