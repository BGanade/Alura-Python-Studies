# List of books with their stock information
books = [
    {"name": "1984", "stock": 5},
    # "Dom Casmurro" is a proper noun, often kept as is.
    {"name": "Dom Casmurro", "stock": 0},
    {"name": "The Little Prince", "stock": 3},
    {"name": "The Hobbit", "stock": 0},
    {"name": "Pride and Prejudice", "stock": 2}
]

for book in books:
    if book["stock"] == 0:
        continue
    print(f"book disponible: {book["name"]}")
