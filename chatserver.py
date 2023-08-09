from socket import *
from threading import Thread

def handle_client(client_socket):
    name = bytes.decode(client_socket.recv(BUFFER_SIZE))
    print(name, "connected")

    while True:
        message = bytes.decode(client_socket.recv(BUFFER_SIZE))
        print(name + ": " + message)
        if message.lower() == "quit":
            print(name, "disconnected")
            break

HOST = '10.60.131.140'  # เปลี่ยนเป็น IP ของเครื่อง server
PORT = 5000
BUFFER_SIZE = 4096

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print('Chat server started on port', PORT)

while True:
    print('Waiting for connection...')
    client, address = server.accept()
    print('...connected from:', address)
    client_handler = Thread(target=handle_client, args=(client,))
    client_handler.start()
