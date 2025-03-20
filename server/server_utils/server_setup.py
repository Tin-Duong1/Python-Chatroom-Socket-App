import socket
from server_utils.auth_utils import *

class Server:
    def __init__(self, host, port, file_path):
        self.host = host
        self.port = port
        self.file_path = file_path
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.client_socket = None  
        print(f"Server is listening on {self.host}:{self.port}")

    def run_server(self):
        usrs = read_users(self.file_path)
        
        while True:
            try:
                print("Waiting for client connection...")
                self.client_socket, addr = self.server.accept() 
                print(f"Client connected from {addr}")
                print("My chat room server. Version One.")
                
                connected = True
                while connected:
                    try:
                        data = self.client_socket.recv(1024).decode()
                        if not data:
                            print("Client disconnected")
                            break
                            
                        print(f"Received command: {data}")
                        args = command_split(data)
                        
                        if command_check(args):
                            if args[0] == "login":
                                if len(args) >= 3:
                                    username = args[1]
                                    password = args[2]
                                    login(self, username, password, usrs)
                                else:
                                    self.client_socket.send("Invalid login format. Use: login <username> <password>".encode())
                                
                            elif args[0] == "newuser":
                                if len(args) >= 3:
                                    username = args[1]
                                    password = args[2]
                                    new_user(self, username, password, self.file_path, usrs)
                                else:
                                    self.client_socket.send("Invalid newuser format. Use: newuser <username> <password>".encode())
                                
                            elif args[0] == "send":
                                if len(args) >= 2:
                                    msg = " ".join(args[1:]) 
                                    send_recieve_msg(self, msg)
                                else:
                                    self.client_socket.send("Invalid send format. Use: send <message>".encode())
                                
                            elif args[0] == "logout":
                                logout(self)
                                connected = False
                        else:
                            self.client_socket.send("Invalid command. Please try again.".encode())
                            
                    except Exception as e:
                        print(f"Error handling client: {e}")
                        connected = False
                        
            except Exception as e:
                print(f"Server error: {e}")
                
            finally:
                if self.client_socket:
                    self.client_socket.close()
                    self.client_socket = None