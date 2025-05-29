import re  # Import the regular expression module

# Get the recipe description from the user
recipe_description = input("Digite a descrição da receita: ")

# Find all numbers in the description.
# Since the problem states "o único número presente", we can safely take the first result.
recipe_number = re.findall(r'\d+', recipe_description)[0]

# Display the found recipe number
print(f"O número da receita é: {recipe_number}")
