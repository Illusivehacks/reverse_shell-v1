# reverse_shell-v1

C&C Server and Target - Illusive_Hacks
Welcome to the Command and Control (C&C) Server and target system by Illusive_Hacks. This system allows a server to send shell commands to connected clients and receive responses back, offering control over remote systems. The C&C server listens on a specified IP and port, while the client establishes a connection to receive and execute commands.

Features

Server Side:

Listen for incoming client connections.
Send commands to the client system.
Receive responses from the client and display them.
Command-line interface (CLI) for inputting commands.


Client Side:

Connect to the C&C server.
Execute shell commands received from the server.
Send the command output back to the server.
Loop to maintain the connection until disconnected.


Installation
Requirements
Python 3.x
Windows PowerShell (on the client-side script)
Administrative privileges (if needed)


Setup Instructions

C&C Server:

Clone or download the project repository.
Make sure Python 3.x is installed on your machine.
Modify the HOST and PORT variables in the server.py file to the desired IP address and port for listening.

Client Script:

Modify the server_ip and server_port variables in the client-side client.bat file to match the server's IP address and port.
Place the client.bat file on the target machine (this can be the same machine or a different one).
Ensure PowerShell is available on the client machine.
