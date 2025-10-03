import datetime
import socket
from datetime import datetime

from time import sleep

if __name__ == "__main__":
    # Define the server address and port
    server_address = ("localhost", 12345)

    # Create a UDP socket
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        messages: int = 10
        client_id: int = datetime.now().microsecond

        for i in range(1, messages + 1):
            # Message to be sent to the server
            message = bytes(f"{client_id}#This is a test message #{i}.", "utf-8")

            # Send the message to the server
            print(f"sending: {message.decode()}")
            sent = udp_client_socket.sendto(message, server_address)

            # Receive response from the server (4096 is the size of the buffer)
            data, server = udp_client_socket.recvfrom(4096)
            print(f"received: {data.decode()}")
            sleep(1)

    finally:
        print("closing the client socket.")
        udp_client_socket.close()
