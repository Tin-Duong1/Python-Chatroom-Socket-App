from server.server_utils.server_setup import Server

def read_users(file_path):
    usrs = set() # Used set here to store users for O(1) lookup through hash function
    with open(file_path, 'r') as file: # opens file in read mode
        for line in file:
            user = line.split(",")[0].strip("()") # split method returns a list splitting on the delimiter, chaining with [0] to get the first element, and strip to remove parenthesis
            usrs.add(user)
    return usrs


def login(server_obj: Server, username: str, password: str, usrs: set):
    
    if username not in usrs:
        return server_obj.client.send("Denied. User name or password incorrect.")
    
    if username in usrs:
        if password != usrs[username]:
            return server_obj.client.send("Denied. User name or password incorrect.")
        else:
            return server_obj.client.send("login confirmed")
        


def new_user(server_obj: Server, username: str, password: str, file_path: str, usrs: set):
    
    if username in usrs:
        return server_obj.client.send("Denied. User account already exists.")
    else:
        with open(file_path, 'w') as file:
            file.write(f"({username}, {password})\n")
            usrs[username] = password
        return server_obj.client.send("New user account created. Please login.")
        
    