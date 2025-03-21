import socket                                                                                # import the socket module according to assignment description
from server_utils.auth_utils import *                                                        # Import the server functions to handle the requests made 

class Server:                                                                                # Server class that handles server socket connection and client requests
    def __init__(self, host, port, file_path):
        self.host = host
        self.port = port
        self.file_path = file_path
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.client_socket = None  
        print("My chat room server. Version One.\n")

    def run_server(self):                                                                    # Method to run the server and handle client requests
        usrs = read_users(self.file_path)                                                    # Current session list of users and it also reads in from the file of previous sessions
        current_usr = ""                                                                     # Var to see who is logged in
        while True:
            try:
                print("Waiting for client connection...")
                self.client_socket, addr = self.server.accept()                              # Accept a client connection
                print(f"Client connected from {addr}")
                
                while True:                                                                  # While the client is connected keep listening for the commands sent from client 
                    try:
                        data = self.client_socket.recv(1024).decode()
                        if not data:
                            print("Client disconnected")
                            break
                            
                        args = command_split(data)                                           # Split the command into a list of args and check how to respond
                        if command_check(args):
                            if args[0] == "login":
                                if len(args) == 3:
                                    username = args[1]
                                    password = args[2]
                                    user_name = login(self, username, password, usrs)         # call the functions set in other file that responds to these requests and check to see if logged in
                                    if user_name:
                                        current_usr = user_name
                                        print(f"{current_usr} login.")
                                
                            elif args[0] == "newuser":                                        # check first arg for command to know how to respond 
                                if len(args) == 3:
                                    username = args[1]
                                    password = args[2]
                                    new_user(self, username, password, self.file_path, usrs)  # Call function set in other file to respond to requests
                                
                            elif args[0] == "send":                                           # check first arg for command to know how to respond 
                                if len(args) >= 2 and current_usr:
                                    msg = " ".join(args[1:]) 
                                    send_msg(self, msg, current_usr)
                                    print (f"{current_usr}: {msg}")
                                else:
                                    self.client_socket.send(">Denied. Please login first.".encode())
                                
                            elif args[0] == "logout":                                          # check first arg for command to know how to respond 
                                logout(self, current_usr)                                      # Call function set in other file to respond to requests
                                print(f"{current_usr} logout.")
                                current_usr = ""
                                break
                            
                    except Exception as e:                                                     # Error handling for exceptions
                        print(f"Error handling client: {e}")
                        
            except Exception as e:
                print(f"Server error: {e}")
                
            finally:
                if KeyboardInterrupt:                                                          # Handle keyboard interrupt for connections and exit
                    if self.client_socket:
                        try:
                            self.client_socket.close()
                        except Exception as e:
                            pass
                    self.client_socket = None