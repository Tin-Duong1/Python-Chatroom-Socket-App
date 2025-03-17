from client_util.client_setup import Client
from client_util.user_util import *

if __name__ == "__main__":
    
    port = 19171
    ip = "127.0.0.1"
    
    client = Client(host=ip, port=port)
    client.connect_client_to_server()
    
    
    while(Client.is_connected):
                
        user_input = input()
        args_list = user_input.split(" ")
        
        if args_list[0] == "login":
            username = args_list[1]
            password = args_list[2]
            login(client, username, password)
            
        elif args_list[0] == "newuser":
            username = args_list[1]
            password = args_list[2]
            new_user(client, username, password)
            
        elif args_list[0] == "send":
            msg = " "
            msg.join(args_list[1:])
            send_recieve_msg(client, msg)
            
        elif args_list[0] == "logout":
            logout(client)
            break
        
