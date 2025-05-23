# Login/Registration System

while True:  # Loop indefinitely until valid inputs are provided
    nickname = input("Enter your nickname: ")
    if len(nickname) < 5:
        print("The nickname must be at least 5 characters.")
        continue  # Go back to the start of the loop to re-enter nickname

    password = input("Enter your password: ")
    if len(password) < 8:
        print("The password must be at least 8 characters.")
        continue  # Go back to the start of the loop to re-enter password

    # If both conditions are met, break out of the loop
    print("Registration completed successfully.")
    break
