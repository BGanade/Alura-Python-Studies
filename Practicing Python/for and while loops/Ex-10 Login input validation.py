login = True
nickname = input("Enter your nickname: ")
password = input("Enter your password: ")
while login:
    if len(nickname) < 5:
        print("The nickname must be at least 5 characters")
        nickname = input("Enter your nickname: ")
    elif len(password) < 8:
        print("The password must be at least 8 characters")
        password = input("Enter your password: ")
    else:
        print("registration completed successfully ")
        login = False
