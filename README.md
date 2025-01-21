# reverse_shell-v1

C&C Server and Target - Illusive_Hacks
Welcome to the Command and Control (C&C) Server and target system by Illusive_Hacks. This system allows a server to send shell commands to connected clients and receive responses back, offering control over remote systems. The C&C server listens on a specified IP and port, while the client establishes a connection to receive and execute commands.

NOTE USE SAME HOST/IP AND PORT IN BOTH SCRIPTS

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



Usage Instructions


Running the Server
Open your terminal or command prompt.
Navigate to the directory where server.py is located.

Run the server script:
bash
````python command_control_server.py````

The server will display a banner and start listening for incoming client connections on the specified IP and port.
Running the Client
Place the client.bat file on the target machine.

Ensure that the client has access to PowerShell and execute the batch script by double-clicking it or running it from the command prompt:
batch
````reverse_shell.bat````
The client will attempt to connect to the server.


Server Commands
Once connected, you can execute commands in the Shell> prompt. Some example commands:

dir 
-List directory contents.

echo Hello  
-Output a message.

exit  
-Disconnect from the client.

ipconfig
-Display IP configuration details of the client machine.

ping [hostname or IP]
Ping a specified host or IP address from the client machine.

tasklist
List all currently running processes on the client.

taskkill /f /im [process_name]
Forcefully terminate a specific process on the client.

systeminfo
Display detailed system information of the client machine.

whoami
Show the current logged-in user on the client machine.

cd [directory]
Change the working directory on the client machine.

mkdir [directory_name]
Create a new directory on the client.

rmdir [directory_name]
Remove an existing directory on the client.

copy [source] [destination]
Copy a file from one location to another on the client.

del [filename]
Delete a file on the client machine.

type [filename]
Display the contents of a file in the terminal.

cls
Clear the screen in the client’s terminal.

shutdown /s /f /t 0
Shutdown the client machine immediately.

restart
Restart the client machine.

netstat
Display the network connections and listening ports on the client.

set
Display all environment variables for the client machine.

ftp [hostname]
Connect to an FTP server from the client machine.

date
Display or set the date on the client machine.

time
Display or set the time on the client machine.


Commands will be sent to the client for execution, and the output will be displayed on the server.

Exiting
To exit the server and stop listening for new connections, simply type:

bash
````exit````


Security Considerations
This setup is intended for educational purposes only. Use responsibly and only in environments where you have permission.
Ensure secure access to your C&C server (e.g., use encryption or VPNs) to prevent unauthorized access.
Always monitor and control the network connections to mitigate risks associated with backdoors or unauthorized access.


Customization
Change the HOST and PORT variables to suit your network environment.
Modify the client-side script to customize command execution or add logging functionality.
Customize the banner or add additional features as needed.


Contributing
Feel free to contribute to this project by submitting issues, pull requests, or suggestions for improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries, contact Illusive_Hacks via email or through GitHub.

Happy Hacking!


