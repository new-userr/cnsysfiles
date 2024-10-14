import socket

def start_server(host='localhost', port=65432):
    """Start the server and handle communication with a single client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        with client_socket:
            while True:
                # Receive message from client
                client_message = client_socket.recv(1024).decode()
                if not client_message:
                    break
                print(f"Client: {client_message}")
                
                # Send message to client
                server_message = input("Server: ")
                client_socket.sendall(server_message.encode())

if __name__ == "__main__":
    start_server()
