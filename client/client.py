from client_util.client_setup import Client                                                          # Import the class Client from other file
from client_util.user_util import *                                                                  # Import all functions from user_util file


def main():                                                                                          # Main function of entry
    port = 19171                                                                                     # Port number 
    ip = "127.0.0.1"                                                                                 # IP address of server
    
    client = Client(host=ip, port=port)                                                              # Create an instance of the Client class passing in the args for the fields
    if not client.connect_client_to_server():                                                        # Use the connect method to connect to the server and check if connection is success
        print(">Failed to connect to server. Exiting.")
        return
    
    print(">Connected to server.\nType commands (login, newuser, send, logout).")                    # show connection message and commands that are available
    
    while client.connection:                                                                         # While the connection is still active
        try:
            user_input = input(">")                                                                  # Get user input 
            if not user_input:
                continue
                
            args_list = user_input.split(" ")                                                        # Split the input into a list of args
            
            if args_list[0] == "login":                                                              # Check first arg for the command to know which function to usen then call the function from the other file
                if len(args_list) == 3:
                    username = args_list[1]                                                          # Pass in the other args from list as the expected params for the function
                    password = args_list[2]                                                          # Repeated for the other 3 commands
                    login(client, username, password)
                else:
                    print(">Incorrect amount of args. Try: login <username> <password>")
                
            elif args_list[0] == "newuser":
                if len(args_list) == 3:
                    username = args_list[1]
                    password = args_list[2]
                    new_user(client, username, password)
                else:
                    print(">Incorrect amount of args. Try: newuser <username> <password>")
                
            elif args_list[0] == "send":
                
                if not client.logged_in:
                    print(">Denied. Please login first.")
                    continue        
                if len(args_list) >= 2:
                    msg = " ".join(args_list[1:])
                    send_recieve_msg(client, msg)
                else:
                    print(">Incorrect amount of args. Try: send <message>")
                
            elif args_list[0] == "logout":
                log_out_success = logout(client)
                if log_out_success:
                    break
                else:
                    print(">logout failed. You may not be logged in.")
            else:
                print(">Unknown command. Try login, newuser, send, logout, exit")
        
        except ConnectionResetError:                                                                 # Error if server shuts down or connection is lost
            print(">Connection to server is lost.")
            client.disconnect()
            break
            
        except BrokenPipeError:
            print(">Connection to server is lost.")
            client.disconnect()
            break
        
        except KeyboardInterrupt:
            print(">Exiting client.")
            client.disconnect()
            break
        
        except Exception as e:
            print(f"Error: {e}")
            client.connection = False
            break
            

    client.client.close()

if __name__ == "__main__":                                                                           # Entry to run main for client
    try: 
        main()
    except KeyboardInterrupt:                                                                        # Handle keyboard interrupt to exit
        print("\n")
        print(">Exiting client.")
        print(">Disconnected from server.")
        exit()
    
