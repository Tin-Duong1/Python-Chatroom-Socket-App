import socket                                                                                     # import the socket module according to assignment description


class Client:                                                                                     # Client class that handels all the client side socket connection 
    
    def __init__(self, host: str, port: str):                                                     # Constructor that initializes with instance parameters host port and the socket connection as well as tracker fields for connection and login status
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = False;
        self.logged_in = False
        
    def connect_client_to_server(self):                                                           # Method to connect client to server and check if connection is successful
        try:
            self.client.connect((self.host, self.port))
            print("My chat room client. Version One.")
            self.connection = True
            return True
        except Exception as e:
            print(f"Error connecting to the server make sure that the server is running.")
            return False
    
    def disconnect(self):                                                                         # disconnect method on error
        self.logged_in = False
        self.connection = False
        try:
            self.client.close()
        except:
            pass
        print(">Server connection lost. Restart the client program to reconnect.")
    
    
    