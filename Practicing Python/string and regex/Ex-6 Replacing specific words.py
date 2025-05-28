import re  # Import the regular expression module

# Get the text to be revised from the user
text_to_revise = input("Enter the text to be revised: ")

# Get the word to be replaced from the user
old_word = input("Which word do you want to replace? ")

# Get the new word from the user
new_word = input("What is the new word? ")

# Use regex to substitute all occurrences of the old word with the new word
# '\b' ensures that only whole words are matched (e.g., 'cat' won't match 'catalogue')
revised_text = re.sub(rf'\b{old_word}\b', new_word, text_to_revise)

# Print the text with the substitutions made
print(revised_text)
