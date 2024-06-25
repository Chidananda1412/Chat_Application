

# Chat Server and Client

This project provides a simple chat server and client application implemented using Python's socket and threading libraries. The server can handle multiple clients, broadcasting messages received from one client to all other connected clients.

## Features

- **Multi-client support**: The server can handle multiple clients simultaneously.
- **Broadcast messaging**: Messages sent by one client are broadcast to all other connected clients.
- **Graceful shutdown**: Clients and server can disconnect gracefully using the `/quit` command.
- **Server commands**: The server can broadcast messages to all clients or shut down using the `/quit` command.

## Installation

Ensure you have Python installed on your system. This project requires Python 3.x.

### Dependencies

This project does not have any external dependencies beyond Python's standard library.

## Usage

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/repositoryname.git
cd Address_to_project_folder
```

### Running the Server

To start the server, run:

```bash
python serverfile.py
```

The server will start listening for incoming client connections on `127.0.0.1:12345`.

### Running the Client

To connect to the server, run:

```bash
python clientfile.py
```

You will be able to enter messages which will be sent to the server and broadcast to all connected clients.

## Server

The server accepts multiple client connections and broadcasts messages to all connected clients except the sender. 

### `handle_client(client_socket, client_address, client_id)`

Handles communication with a connected client.

### `broadcast(message, sender_id=None)`

Broadcasts a message to all connected clients except the sender.

### `remove_client(client_socket)`

Removes a disconnected client from the list of clients.

### `handle_server_input()`

Handles server-side input for broadcasting messages or shutting down the server.



## Client

The client connects to the server, sends messages, and receives broadcast messages from the server.

### `receive_messages()`

Continuously receives messages from the server and displays them.

### `send_message()`

Allows the user to input and send messages to the server.





## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [Chidanand A] at [chidananda1412@gmail.com].


