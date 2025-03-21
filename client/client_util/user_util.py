from client_util.client_setup import Client                                    # Import the class Client from other file

def login(client_obj: Client, username: str, password: str):                   # Client login function that first checks if client is connected to server and if logged in to restrict commands 
    
    if not client_obj.connection:
        print(">Not connected to server")
        client_obj.disconnect()                                                        # Disconnect if not connected to server
        return
    
    if client_obj.logged_in:
        print(">Already logged in")
        return
    
    login_msg = f"login {username} {password}"                                 # This var holds the format string that will be sent with the command and user and password
    
    try:
        client_obj.client.send(login_msg.encode())                             # Sends the login to the server
        response = client_obj.client.recv(1024).decode()                       # Receives the response from the server
        if "confirmed" in response:                                            # Checks if the response has the the confirmation word in to set success login flag
            client_obj.logged_in = True
            print(response)                                                    # show response on client side
        else:
            print(response)                                                    # Otherwise show response without setting the flag or unsucessful login
            client_obj.logged_in = False                                       # Just to make sure that it is not set to true
    except BrokenPipeError:
        print(">Connection to server is lost.")
        client_obj.disconnect()                                                        # Disconnect if the connection is lost    
    except ConnectionResetError:
        print(">Connection to server is lost.")
        client_obj.disconnect()
    except Exception as e:                                                     # Error handling for exceptions that can occur
        print(f">Error during login: {e}")
        client_obj.logged_in = False


def new_user(client_obj: Client, username: str, password: str):                # new user function with the same checks as login and also restriction checks for command 
    
    if not client_obj.connection:                                     
        print(">Not connected to server")
        client_obj.disconnect()                                                        # Disconnect if not connected to server
        return
    
    if client_obj.logged_in:
        print(">Already logged in")
        return
    
    if len(username) < 3 or len(username) > 32:                                # Check len of message to restricting chars for username and password between 3 and 32 and 4 and 8 for password 
        return ">Username must be between 3 and 32 characters"
    
    if len(password) < 4 or len(password) > 8:
        return ">Password must be between 4 and 32 characters"
    
    register_msg = f"newuser {username} {password}"
    try:
        client_obj.client.send(register_msg.encode())                              # Format var to send if command is correctly formatted and conditions are met                            # Send the format message to the server
        response = client_obj.client.recv(1024).decode()                           # Receive the response from the server
        print(response)                                                            # Print response on client side
    except BrokenPipeError:
        print(">Connection to server is lost.")
        client_obj.disconnect()
    except ConnectionResetError:
        print(">Connection to server is lost.")
        client_obj.disconnect()
    except Exception as e:                                                         # Error handling for exceptions that can occur
        print(f">Error during new user : {e}")
        
        
def send_recieve_msg(client_obj: Client, msg: str):                            # Function for the send command with same checks again and restrictions for msg
    
    if not client_obj.connection:                                                # Check if client is connected to server
        print(">Not connected to server")
        client_obj.disconnect()                                                    # Disconnect if not connected to server
        return
    if not client_obj.logged_in:
        print(">Denied. Please login first.")
    elif len(msg) < 1 or len(msg) > 256:
        print(">Message must be between 1 and 256 characters")
    elif client_obj.logged_in:
        try:
            formatted_msg = f"send {msg}"                                      # Format the message with send command and the 
            client_obj.client.send(formatted_msg.encode())
            response = client_obj.client.recv(1024).decode()                   # Response from server
            print(response)                                                    # Print response on client side
        except BrokenPipeError:
            print(">Connection to server is lost.")
            client_obj.disconnect()                                            # Disconnect if the connection is lost
        except ConnectionResetError:
            print(">Connection to server is lost.")
            client_obj.disconnect()
        except Exception as e:                                                 # Error handling for exceptions that can occur
            print(f">Error sending message: {e}")
            client_obj.connection = False
    

def logout(client_obj: Client):                                                # Logout function with the error and restriction checks for flags and connection
    
    if not client_obj.connection:
        print(">Not connected to server")
        client_obj.disconnect()                                                    # Disconnect if not connected to server
        return
    
    if not client_obj.logged_in:
        print(">Not logged in")
        return
    
    try:
        client_obj.client.send("logout".encode())                             # Send the logout command to the server
        response = client_obj.client.recv(1024).decode()                      # Receive the response from the server
        print(response)                                                       # Print response on client side
        client_obj.logged_in = False                                          # Set the logged in flag to false
        client_obj.connection = False                                         # Set the connection flag to false
        client_obj.client.close()                                             # Close the client socket
        return True
        
    except BrokenPipeError:                                                                   # Error handling for exceptions that can occur
        client_obj.connection = False
        client_obj.logged_in = False
        client_obj.client.close()
    
    except ConnectionResetError:
            print(">Connection to server is lost.")
            client_obj.disconnect()

    except Exception as e:
        print(f">Error during logout: {e}")                                      # Print error message
        client_obj.connection = False
        client_obj.logged_in = False
        client_obj.client.close()                                                 # Close the client socket
    