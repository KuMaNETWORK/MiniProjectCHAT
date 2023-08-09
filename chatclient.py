from socket import *

HOST = '10.60.131.140'  # เปลี่ยนเป็น IP ของเครื่อง server ที่เชื่อมต่อกับ
PORT = 5000

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")
client.send(str.encode(name))

while True:
    message = input("Enter your message: ")
    if message.lower() == "quit":
        client.send(str.encode(message))
        print("Goodbye!")
        break
    client.send(str.encode(message))
