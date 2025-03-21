from client_util.client_setup import Client
from client_util.user_util import *


def main():
    port = 19171
    ip = "127.0.0.1"
    
    client = Client(host=ip, port=port)
    if not client.connect_client_to_server():
        print(">Failed to connect to server. Exiting.")
        return
    
    print(">Connected to server.\nType commands (login, newuser, send, logout).")
    
    while client.connection:
        try:
            user_input = input(">")
            if not user_input:
                continue
                
            args_list = user_input.split(" ")
            
            if args_list[0] == "login":
                if len(args_list) == 3:
                    username = args_list[1]
                    password = args_list[2]
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
                    print(">You must be logged in to send messages.")
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
                
        except Exception as e:
            print(f"Error: {e}")
            client.connection = False
            
    print(">Disconnected from server.")
    client.client.close()

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\n")
        print(">Exiting client.")
        exit()
    
