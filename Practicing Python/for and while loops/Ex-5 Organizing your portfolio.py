# Analyze and print project names

projects = ["website", "game", "data analysis", None, "mobile application"]

# Iterate through each project in the list
for project in projects:
    # If the project is None, skip to the next iteration
    if project == None:
        continue
    # Print the project name
    print(project)
