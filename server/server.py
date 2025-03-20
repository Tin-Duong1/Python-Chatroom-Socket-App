import os

from server_utils.auth_utils import *
from server_utils.server_setup import Server
                   
def main():
    ip = "127.0.0.1" 
    port = 19171 
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    usrs_txt_filepath = os.path.join(current_dir, "user_auth", "users.txt")
    
    os.makedirs(os.path.dirname(usrs_txt_filepath), exist_ok=True)
    
    if not os.path.exists(usrs_txt_filepath):
        with open(usrs_txt_filepath, 'w') as f:
            f.write("(Tom, Tom11)\n")
            f.write("(David, David22)\n")
            f.write("(Beth, Beth33)\n")
    
    server_init = Server(host=ip, port=port, file_path=usrs_txt_filepath)
    server_init.run_server()
    
if __name__ == "__main__":
    main()


