from socket import *
from threading import Thread

HOST = '10.60.131.140'  # เปลี่ยนเป็น IP ของเครื่อง server ที่เชื่อมต่อกับ
PORT = 5000
BUFFER_SIZE = 4096  # กำหนดขนาดของ buffer

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")
client.send(str.encode(name))

def receive_messages():
    while True:
        message = bytes.decode(client.recv(BUFFER_SIZE))
        print(message)

receive_thread = Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    if message.lower() == "quit":
        client.send(str.encode(message))
        print("Goodbye!")
        break
    client.send(str.encode(message))
