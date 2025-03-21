from client_util.client_setup import Client

def login(client_obj: Client, username: str, password: str):
    
    if not client_obj.connection:
        print(">Not connected to server")
        return
    
    if client_obj.logged_in:
        print(">Already logged in")
        return
    
    login_msg = f"login {username} {password}"
    
    try:
        client_obj.client.send(login_msg.encode())
        response = client_obj.client.recv(1024).decode()
        if "confirmed" in response: 
            client_obj.logged_in = True
            print(response)
        else:
            print(response)
            client_obj.logged_in = False
        
    except Exception as e:
        print(f">Error during login: {e}")
        client_obj.logged_in = False


def new_user(client_obj: Client, username: str, password: str):
    
    if not client_obj.connection:
        print(">Not connected to server")
        return
    
    if client_obj.logged_in:
        print(">Already logged in")
        return
    
    if len(username) < 3 or len(username) > 32:
        return ">Username must be between 3 and 32 characters"
    
    if len(password) < 4 or len(password) > 8:
        return ">Password must be between 4 and 32 characters"
    
    register_msg = f"newuser {username} {password}"
    client_obj.client.send(register_msg.encode())
    
    response = client_obj.client.recv(1024).decode()
    print(response)
    

def send_recieve_msg(client_obj: Client, msg: str):
    
    if client_obj.logged_in:
        try:
            formatted_msg = f"send {msg}"
            client_obj.client.send(formatted_msg.encode())
            response = client_obj.client.recv(1024).decode()
            print(response)
        except Exception as e:
            print(f">Error sending message: {e}")
            client_obj.connection = False
    else:
        print(">Denied. Please login first.")
                       

def logout(client_obj: Client):
    
    if not client_obj.connection:
        print(">Not connected to server")
        return
    
    if not client_obj.logged_in:
        print(">Not logged in")
        return
    
    try:
        client_obj.client.send("logout".encode())
        response = client_obj.client.recv(1024).decode()
        print(response)
        client_obj.logged_in = False
        client_obj.connection = False
        client_obj.client.close()
        return True
        
    except:
        client_obj.connection = False
        client_obj.logged_in = False
        client_obj.client.close()
    