import socket
import threading
from time import ctime

host = '192.168.255.1'                                                 
port = 3000                                                      
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
server.bind((host, port))                                          
server.listen()                                                   

clients = [] 
nicknames = []

def broadcast(message): 
    for client in clients:
        client.send(message)                                       

def connect_to_server_3():
    server3_host = '192.168.255.1'
    server3_port = 3000

    client3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to Server 3 at {server3_host}:{server3_port}...")
    client3.connect((server3_host, server3_port))

    # ทำอะไรก็ตามที่ต้องการกับ server 3

    client3.close()
    print("Disconnected from Server 3.")


def handle(client):
    try:
        while True:
            message = client.recv(1024)
            if message.decode('ascii') == "quit":
                client.send('You have disconnected.'.encode('ascii'))
                client.close()
                print('{} has disconnected.'.format(nickname))
                break
            elif message.decode('ascii') == "leave":
                client.send('Leaving to server 3...'.encode('ascii'))
                client.close()
                connect_to_server_3()  # เรียกฟังก์ชันที่เชื่อมต่อ server 3
                break
            else:
                broadcast(message)
    except:
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        broadcast('{} Disconnect!'.format(nickname).encode('ascii'))
        nicknames.remove(nickname)
        client.close()
        print('{} has Disconnected .'.format(nickname) +' '+ctime())  

def receive():
    while True:
        client, address = server.accept()                          
        print("Connected with {}".format(str(address)+ ' '+ctime()))   

        client.send('NICK'.encode('ascii'))                       
        nickname = client.recv(1024).decode('ascii')                
        nicknames.append(nickname)
        clients.append(client)

        print("Name is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))   
        client.send('Connected to server!'.encode('ascii'))        

        thread = threading.Thread(target=handle, args=(client,))   
        thread.start()                                             

print("Lobby is started..............,:) ")
receive()
