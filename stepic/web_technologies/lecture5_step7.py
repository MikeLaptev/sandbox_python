import socket
import _thread


def handle(c, a):
    while True:
        data = c.recv(1024)
        if data == 'close':
            c.close()
            break
        c.send(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 2222))
server.listen(10)

while True:
    conn, addr = server.accept()
    _thread.start_new_thread(handle, (conn, addr))
