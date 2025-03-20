import socket

class Client:
    
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = False;
        self.logged_in = False
        
    def connect_client_to_server(self):
        try:
            self.client.connect((self.host, self.port))
            print("My chat room client. Version One.")
            self.connection = True
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    
    