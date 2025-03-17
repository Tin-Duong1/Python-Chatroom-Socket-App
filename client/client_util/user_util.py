from client_setup import Client

def login(client_obj: Client, username: str, password: str):
    
    if not client_obj.connection:
        print("Not connected to server")
        return
    
    if client_obj.logged_in:
        print("Already logged in")
        return
    
    login_msg = f"login {username} {password}"
    
    client_obj.client.send(login_msg.encode())
    
    response = client_obj.client.recv(1024).decode()
    
    if response == "login confimed":
        client_obj.logged_in = True
        print(response)
    else:
        print(response)


def new_user(client_obj: Client, username: str, password: str):
    
    if not client_obj.connection:
        print("Not connected to server")
        return
    if client_obj.logged_in:
        print("Already logged in")
        return
    
    if len(username) < 3 or len(username) > 32:
        return "Username must be between 3 and 32 characters"
    
    if len(password) < 4 or len(password) > 8:
        return "Password must be between 4 and 32 characters"
    
    register_msg = f"register {username} {password}"
    client_obj.client.send(register_msg.encode())
    
    response = client_obj.client.recv(1024).decode()
    print(response)
    

def send_recieve_msg(client_obj: Client, msg: str):
    if client_obj.logged_in:
        client_obj.client.send(msg.encode())
        response = client_obj.client.recv(1024).decode()
        print(response)
                       

def logout(client_obj: Client):
    
    if not client_obj.connection:
        print("Not connected to server")
        return
    
    if not client_obj.logged_in:
        print("Not logged in")
        return
    
    client_obj.client.send("logout".encode())
    response = client_obj.client.recv(1024).decode()
    print(response)
    client_obj.logged_in = False