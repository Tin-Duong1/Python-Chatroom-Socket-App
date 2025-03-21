import os

from server_utils.auth_utils import *
from server_utils.server_setup import Server
                   
def main():                                                                          # Main function of entry point for server
    ip = "127.0.0.1"                                                                 # IP address
    port = 19171                                                                     # Port number 
    
    current_dir = os.path.dirname(os.path.abspath(__file__))                        # Get path of curr dir 
    usrs_txt_filepath = os.path.join(current_dir, "user_auth", "users.txt")         # make path to where the file needs to be created or read from
    
    os.makedirs(os.path.dirname(usrs_txt_filepath), exist_ok=True)                  # Create the directory if it does not exist
    
    if not os.path.exists(usrs_txt_filepath):                                       # If doesnt exists write with defaults credentials 
        with open(usrs_txt_filepath, 'w') as f:
            f.write("(Tom, Tom11)\n")
            f.write("(David, David22)\n")
            f.write("(Beth, Beth33)\n")
    
    server_init = Server(host=ip, port=port, file_path=usrs_txt_filepath)           # Create instance of the server class and pass in args for connection and fields
    server_init.run_server()                                                        # Call the run method in class to run and listen (This is the one with the while until connection breaks)
    
if __name__ == "__main__":
    try:
        main()                                                                      # Run main
    except KeyboardInterrupt:                                                       # Handles keyboard interrrupt
        print("\nServer shutting down...")
        print("Server closed.")
    except Exception as e:
        print(f"Error: {e}")


