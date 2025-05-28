# Get URL from user for validation
url = input("Enter the URL for validation: ")

# Check if the URL starts with "https://" and ends with ".com"
if url.startswith("https://") and url.endswith(".com"):
    # If both conditions are met, the URL is considered valid
    print("Valid URL!")
else:
    # Otherwise, the URL is considered invalid
    print("Invalid URL!")
