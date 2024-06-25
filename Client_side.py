import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == '/quit':
                print("Server has closed the connection.")
                client_socket.close()
                break
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            break

def send_message():
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
            if message == '/quit':
                print("Disconnecting from the server...")
                client_socket.close()
                break
        except Exception as e:
            print(f"Error sending message: {e}")
            client_socket.close()
            break

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_message()
