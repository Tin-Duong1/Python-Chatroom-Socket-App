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
        print("My chat room server. Version One.\n")

    def run_server(self):
        usrs = read_users(self.file_path)
        current_usr = ""
        while True:
            try:
                print("Waiting for client connection...")
                self.client_socket, addr = self.server.accept()
                print(f"Client connected from {addr}")
                
                while True:
                    try:
                        data = self.client_socket.recv(1024).decode()
                        if not data:
                            print("Client disconnected")
                            break
                            
                        args = command_split(data)
                        if command_check(args):
                            if args[0] == "login":
                                if len(args) == 3:
                                    username = args[1]
                                    password = args[2]
                                    user_name = login(self, username, password, usrs)
                                    if user_name:
                                        current_usr = user_name
                                        print(f"{current_usr} login.")
                                else:
                                    self.client_socket.send(">Invalid login format. Use: login <username> <password>".encode())
                                
                            elif args[0] == "newuser":
                                if len(args) == 3:
                                    username = args[1]
                                    password = args[2]
                                    new_user(self, username, password, self.file_path, usrs)
                                else:
                                    self.client_socket.send(">Invalid newuser format. Use: newuser <username> <password>".encode())
                                
                            elif args[0] == "send":
                                if len(args) >= 2:
                                    msg = " ".join(args[1:]) 
                                    send_msg(self, msg, current_usr)
                                    print (f"{current_usr}: {msg}")
                                else:
                                    self.client_socket.send(">Invalid send format. Use: send <message>".encode())
                                
                            elif args[0] == "logout":
                                logout(self, current_usr)
                                print(f"{current_usr} logged out.")
                                current_usr = ""
                                break
                        else:
                            self.client_socket.send(">Invalid command. Please try again.".encode())
                            
                    except Exception as e:
                        print(f"Error handling client: {e}")
                        
            except Exception as e:
                print(f"Server error: {e}")
                
            finally:
                if KeyboardInterrupt:
                    if self.client_socket:
                        try:
                            self.client_socket.close()
                        except Exception as e:
                            pass
                    self.client_socket = None