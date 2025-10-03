import socket
from typing import Dict, List, Tuple


class Game:

    def __init__(self):
        self.users: Dict[str, User] = {}

    def has_user(self, user_id: str):
        return user_id in self.users


class User:

    def __init__(self, user_id: str):
        self.user_id: str = user_id
        self.questions: List[Tuple[str, str]] = []


if __name__ == "__main__":
    # Define the server address and port
    server_address = ("localhost", 12345)

    # Create a UDP socket
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    udp_server_socket.bind(server_address)

    print(f"UDP server listening on {server_address[0]}:{server_address[1]}")

    game = Game()

    while True:
        # Wait for a connection (receive data). 4096 is the size of the buffer.
        data, client_address = udp_server_socket.recvfrom(4096)
        print(f"received [{data.decode()}] from [{client_address}]")

        d = data.decode()
        if "#" not in d:
            print(f"malformed data...")
            # Optionally, send a response back to the client
            response = f"malformed answer"
            udp_server_socket.sendto(response.encode(), client_address)
        else:
            client_id, message = d.split("#", 1)
            # Optionally, send a response back to the client
            response = f"received message: [{message}] from client [{client_id}]"
            udp_server_socket.sendto(response.encode(), client_address)
