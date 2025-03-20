class Server:  
    pass

def command_split(command: str)-> list:
    return command.split(" ")


def command_check(args: list)-> bool:
    if not args:
        return False
        
    if args[0] == "login":
        if len(args) >= 3:
            return True
        else:
            return False
    elif args[0] == "newuser": 
        if len(args) >= 3:  
            return True
        else:
            return False
    elif args[0] == "send":
        if len(args) >= 2:
            return True
        else:
            return False
    elif args[0] == "logout":
        if len(args) >= 1:
            return True
        else:
            return False
    else:
        return False
        

def read_users(file_path):
    usrs = {} 
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.strip('()').split(',')
                    if len(parts) >= 2:
                        username = parts[0].strip()
                        password = parts[1].strip()
                        usrs[username] = password
    except FileNotFoundError:
        print(f"Warning: User file {file_path} not found. Starting with empty user list.")
    return usrs


def login(server_obj: Server, username: str, password: str, usrs: dict):
    
    if username not in usrs:
        return server_obj.client_socket.send("Denied. User name or password incorrect.".encode())
    
    if username in usrs:
        if password != usrs[username]:
            return server_obj.client_socket.send("Denied. User name or password incorrect.".encode())
        else:
            return server_obj.client_socket.send("login confirmed".encode())
        

def send_recieve_msg(server_obj: Server, msg: str):
    return server_obj.client_socket.send(msg.encode())


def new_user(server_obj: Server, username: str, password: str, file_path: str, usrs: dict):
    
    if username in usrs:
        return server_obj.client_socket.send("Denied. User account already exists.".encode())
    else:
        with open(file_path, 'w') as file:
            file.write(f"({username}, {password})\n")
            usrs[username] = password
        return server_obj.client_socket.send("New user account created. Please login.".encode())
        
        
def logout(server_obj: Server):
    return server_obj.client_socket.send("".encode())
