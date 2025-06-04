# Pantry inventory check

# Define a list of items currently in the pantry
pantry = ['rice', 'beans', 'oil']

# Ask the user to enter an item to check
item = input("Enter the item you want to check: ")

# Check if the entered item is already in the pantry list
if item in pantry:
    # If the item is found, inform the user it's available
    print(f"The item {item} is available in the pantry.")
else:
    # If the item is not found, inform the user it needs to be bought
    print(f"The item {item} needs to be bought.")

# Print the current contents of the pantry (for reference)
print(pantry)
