import socket # Import the python socket module


class Server: # OOP opproach for application
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

    def run(self):
        while True:
            client, address = self.server.accept()
            print(f"Connection from {address} is successful!")
            client.send("Welcome to the chatroom to start by typing in the command line".encode())
            client.close()