# List of books with their stock information
books = [
    {"name": "1984", "stock": 5},
    # "Dom Casmurro" is a proper noun, often kept as is.
    {"name": "Dom Casmurro", "stock": 0},
    {"name": "The Little Prince", "stock": 3},
    {"name": "The Hobbit", "stock": 0},
    {"name": "Pride and Prejudice", "stock": 2}
]

# Iterate through each book dictionary in the 'books' list
for book in books:
    # Check if the 'stock' value of the current book is 0
    if book["stock"] == 0:
        # If stock is 0, skip the rest of the current iteration and move to the next book
        continue
    # If stock is not 0 (i.e., it's greater than 0), print the book's name
    # Corrected: Using single quotes for the dictionary key 'name' inside the f-string
    print(f"Book available: {book['name']}")
