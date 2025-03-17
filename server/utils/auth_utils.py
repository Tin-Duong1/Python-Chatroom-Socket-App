
def read_users(file_path):
    usrs = set() # Used set here to store users for O(1) lookup through hash function
    with open(file_path, 'r') as file: # opens file in read mode
        for line in file:
            user = line.split(",")[0].strip("()") # split method returns a list splitting on the delimiter, chaining with [0] to get the first element, and strip to remove parenthesis
            usrs.add(user)
    return usrs


def login(username: str, password: str, usrs: set):
    
    if username not in usrs:
        return "Invalid username"
    
    if username in usrs:
        if password != usrs[username]:
            return "Invalid password"
        else:
            return "Login successful"
        
    return "Something went wrong and function did not work as expected"


def register(username: str, password: str, file_path: str, usrs: set):
    
    if username in usrs:
        return "Username already exists"
    else:
        with open(file_path, 'w') as file:
            file.write(f"({username}, {password})\n")
            usrs[username] = password
        return "Registration successful"
        
    