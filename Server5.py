import socket
import threading
from time import ctime

host = '192.168.38.238'                                                 
port = 5000                                                      
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
server.bind((host, port))                                          
server.listen()                                                   

clients = [] 
nicknames = []

def broadcast(message): 
    for client in clients:
        client.send(message)                                       

def handle(client):
    try:
        while True:
            message = client.recv(1024)
            if message.decode('ascii') == "quit":
                client.send('You have disconnected.'.encode('ascii'))
                client.close()
                print('{} has disconnected.'.format(nickname))
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

print("Server 5 is started..............,:) ")
receive()
