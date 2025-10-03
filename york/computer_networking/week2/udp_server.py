import socket

if __name__ == "__main__":
    # Define the server address and port
    server_address = ("localhost", 12345)

    # Create a UDP socket
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    udp_server_socket.bind(server_address)

    print(f"UDP server listening on {server_address[0]}:{server_address[1]}")

    while True:
        # Wait for a connection (receive data). 4096 is the size of the buffer.
        data, client_address = udp_server_socket.recvfrom(4096)
        print(f"Received {data.decode()} from {client_address}")

        # Optionally, send a response back to the client
        response = f"Data received: {data.decode()}"
        udp_server_socket.sendto(response.encode(), client_address)
