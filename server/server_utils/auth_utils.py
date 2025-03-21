class Server:                                                                      # This is for type checking 
    pass

def command_split(command: str)-> list:                                            # Function to split the commands again from client to server 
    return command.split(" ")

def command_check(args: list)-> bool:                                              # Function to double-check if the command is valid and has the correct amount of args for each command
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
        
        
def read_users(file_path: str)-> dict:                                              # Function to initially read in from file when program starts to update the dict from prev sess 
    usrs = {}                                                                       # Decided to use a dict since it has faster search in o(1)
    try:
        with open(file_path, 'r') as file:                                          # Open the file in read mode and read each line to have updated usrs sess on start of server 
            for line in file:
                line = line.strip()
                if line:
                    parts = line.strip('()').split(',')
                    if len(parts) >= 2:
                        username = parts[0].strip()
                        password = parts[1].strip()
                        usrs[username] = password
    except FileNotFoundError:
        print(f"File {file_path} not found. Starting with empty user list.")
    return usrs                                                                                  # Return the dict of usrs for updated usrs to search for the new session


def login(server_obj: Server, username: str, password: str, usrs: dict):                         # Function to respond to the client send and see if username and password are correct 
    
    if username not in usrs:                                                                     # Check to see if user is in the dict if not then usr is not registered and sends deny
        server_obj.client_socket.send(">Denied. User name or password incorrect.".encode())
        return None
    
    if username in usrs:                                                                         # If user is in the dict then check if password is correct if not send back deny
        if password != usrs[username]:
            server_obj.client_socket.send(">Denied. User name or password incorrect.".encode())
            return None 
        else:                                                                      # Else everything is good and user is logged in and returns username to keep who is logged in
            server_obj.client_socket.send(">login confirmed".encode())
            return username
        

def send_msg(server_obj: Server, msg: str, current_usr: str):                      # This sends back client to print from the send command and format with the current user logged in
    combined_msg = f">{current_usr}: {msg}"
    return server_obj.client_socket.send(combined_msg.encode())


def new_user(server_obj: Server, username: str, password: str, file_path: str, usrs: dict):    # Function to create new user and puts it in the active dictionary as well as write to file and read in on start 
    
    if username in usrs:                                                                       # Check to see if user is already registered if so send deny back
        return server_obj.client_socket.send(">Denied. User account already exists.".encode())
    else:
        with open(file_path, 'a') as file:                                                     # Use append mode to keep past users and add new one between sessions
            file.write(f"({username}, {password})\n")                                          # Write the new user to the file in the correct format
            usrs[username] = password                                                          # Keep in current session dict to check for login on current sess
            print("New user account created.")
        return server_obj.client_socket.send(">New user account created. Please login.".encode())   # On success send back
        
        
def logout(server_obj: Server, current_usr: str):                                              # Sends confirm that client is logged out
    return server_obj.client_socket.send(f">{current_usr} left".encode())
