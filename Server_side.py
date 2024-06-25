import socket
import threading

def handle_client(client_socket, client_address, client_id):
    print(f"Connected with Client {client_id} at {client_address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message == '/quit':
                print(f"Client {client_id} at {client_address} disconnected.")
                break
            print(f"Received from Client {client_id}: {message}")
            broadcast(f"Client {client_id}: {message}", client_id)
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    remove_client(client_socket)

def broadcast(message, sender_id=None):
    sender_identifier = f"Client {sender_id}" if sender_id else "Server"
    full_message = f"{sender_identifier}: {message}"
    for client_socket, client_id in clients:
        if client_id != sender_id:
            try:
                client_socket.send(full_message.encode())
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client_socket.close()
                remove_client(client_socket)

def remove_client(client_socket):
    for index, (c_socket, c_id) in enumerate(clients):
        if c_socket == client_socket:
            clients.pop(index)
            break

def handle_server_input():
    while True:
        message = input()
        if message == '/quit':
            broadcast("/quit")
            for client_socket, _ in clients:
                client_socket.close()
            server_socket.close()
            print("Server shut down.")
            break
        broadcast(message)

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

clients = []
next_client_id = 1

server_input_thread = threading.Thread(target=handle_server_input)
server_input_thread.start()

while True:
    try:
        client_socket, client_address = server_socket.accept()
        clients.append((client_socket, next_client_id))
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, next_client_id))
        client_thread.start()
        next_client_id += 1
    except Exception as e:
        print(f"Error accepting connections: {e}")
        break
