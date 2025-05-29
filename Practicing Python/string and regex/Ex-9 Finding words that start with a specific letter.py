import re  # Import the regular expression module

# Get the string containing book titles from the user
book_titles = input("Enter the book titles: ")

# Get the initial letter to search for from the user
initial_letter = input("Enter the initial letter to search for: ")

# Find all words that start with the given initial letter.
# - r'...' for raw string.
# - f'...' for f-string to embed 'initial_letter'.
# - \b for word boundary (ensures it's the start of a word).
# - [a-zà-ÿ]* matches zero or more lowercase letters, including common accented Portuguese characters.
# - re.IGNORECASE makes the search case-insensitive.
found_words = re.findall(
    rf'\b{initial_letter}[a-zà-ÿ]*', book_titles, re.IGNORECASE)

# Print the list of all words found
print(found_words)
