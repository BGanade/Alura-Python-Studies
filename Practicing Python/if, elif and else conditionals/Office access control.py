# Access Time Checker

current_hour = int(input("Enter the current hour (24-hour format): "))
min_allowed_hour = 8
max_allowed_hour = 18

if min_allowed_hour <= current_hour <= max_allowed_hour:
    print("Access Granted.")
else:
    print("Access Denied.")
