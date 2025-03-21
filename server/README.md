# Socket Server Application (Python)

- **Tin Duong**
- **03/20**

## Project Description:

This is the server application of the socket project, it is a server that allows for connections and responds to requests. It lets the client send requests and listens and responds according to the command that was sent. This application right now allows for one client connection and has response functions to check for login, newuser and send and logout requests. The application also stores user logins and credentials in a user.txt file that gets read into a dictionary on startup allowing maintaining login through sessions. The server application logs the actions of responses as well in its own terminal.

## Socket API Usage:

The server application uses the socket api in the server_utils folder which consists of functions that utilizes the socket api to send responses and also checks for their validity and also the server class which listens to incoming requests from client connections.

## How to run the client application:

# Setup

- Built on python v13.3.2, ensure a newer build of python is installed that supports the built in latest socket api and also syntax for compatibility
- Code editer or terminal that supports running py files
- The server application needs to be ran first to establish the server for client program to connect.
- The user.txt file is located inside of user_auth folder once created on startup

# Running the server program:

- Open the extracted and ensure the correct path for server folder (.../.../.../server) to find the server.py program to run
- Ensure the path is inside the directory of the parent server folder not inside the server_utils folder
- Ensure the python path is correct as well and run in the current termina
- Run in command line (depending on what OS and python version is installed for MacOS I use the first one since that is how the alias was set on install):

```bash
python3 server.py
```

or

```bash
python server.py
```

# To shut down server:

- CTRL + C
