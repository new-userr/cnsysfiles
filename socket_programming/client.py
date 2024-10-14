import socket

def start_client(host='localhost', port=65432):
    """Connect to the server and handle communication with it."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the server.")

        while True:
            # Send message to server
            client_message = input("Client: ")
            client_socket.sendall(client_message.encode())
            
            # Receive message from server
            server_message = client_socket.recv(1024).decode()
            if not server_message:
                break
            print(f"Server: {server_message}")

if __name__ == "__main__":
    start_client()
