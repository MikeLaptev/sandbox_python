import socket


if __name__ == "__main__":
    # Define the server address and port
    server_address = ("localhost", 12345)

    # Create a UDP socket
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Message to be sent to the server
        message = b"This is a test message."

        # Send the message to the server
        print(f"Sending: {message.decode()}")
        sent = udp_client_socket.sendto(message, server_address)

        # Receive response from the server (4096 is the size of the buffer)
        data, server = udp_client_socket.recvfrom(4096)
        print(f"Received: {data.decode()}")

    finally:
        print("Closing the client socket.")
        udp_client_socket.close()
