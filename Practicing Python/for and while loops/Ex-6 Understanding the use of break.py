# Search for a specific book in the list

books = ["1984", "Dom Casmurro", "The Little Prince",
         "The Hobbit", "Pride and Prejudice"]

# Iterate through each book in the list
for book in books:
    # Check if the current book is "The Hobbit"
    if book == "The Hobbit":
        # If found, print a confirmation message
        print(f"Book found: {book}")
        # Exit the loop immediately after finding the book
        break
