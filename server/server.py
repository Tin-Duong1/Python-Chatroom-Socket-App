from server.utils.auth_utils import *
from server.utils.server_setup import Server
                      
if __name__ == "__main__":
    
    ip = "127.0.0.1" # IP for the server based on the assignment description
    port = 19171 # Port for server based on PawPrint
    usrs_txt_filepath = "server/user_auth/users.txt" # Filepath to the users.txt file
    
    server_init = Server(host=ip, port=port) # Init instance of the server with the host and port
    server_init.run_server() # Run the server with the run method
    
    
    