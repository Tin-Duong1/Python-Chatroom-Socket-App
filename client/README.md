# Socket Client Application (Python)

- **Tin Duong**
- **03/20** 


## Project Description:
This is the client application of the socket project, It lets a user connect to the application and allows for commands through the command line. It establishes a connection with a already running server if there is one and sends to the server application that responds. The client then recieved these responses and displays these on the client side. The client application mainly verifies these commands and checks to ensure that appropriate commands are followed and then sends it to the server application for processing. 

## Socket API Usage:
The client application uses the socket api in the client util folder which consists of functions that utilizes the socket api to send requests and also the client class which uses it for the connection with server. The files inside here are for implementing the code for the communication which utilizes the socket api.

## How to run the client application:
# Setup
- Built on python v13.3.2, ensure a newer build of python is installed that supports the built in latest socket api and also syntax for compatibility
- Code editer or terminal that supports running py files 
- The client application requires that the server application is available for connections so ensuring that the server is ran first is important for a succesful connection

# Running the client program:
- Open the client program and ensure the correct path for client folder (.../.../.../client) to find the client.py program
- Ensure the path is inside the directory of the parent client folder not inside the client_util folder
- Ensure the python path is correct as well and run 
- Run in command line (depending on which OS and python version is installed for MacOS I use the first one since that is how the alias was set on install): 

```bash
python3 client.py
```
or 

```bash
python client.py
```

# Commands to send to server:
- login <username> <password>
- send <msg>
- newuser <username> <password>
-logout