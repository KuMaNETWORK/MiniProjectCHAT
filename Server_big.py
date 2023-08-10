
import socket
import threading
from time import ctime

host = '10.60.131.140'                                                 
port = 10000                                                      
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
server.bind((host, port))                                          
server.listen()                                                   

clients = [] 
nicknames = []

def broadcast(message): 
    for client in clients:
        client.send(message)                                       

def handle(client, nickname):
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
        nicknames.pop(index)
        broadcast('{} Disconnect!'.format(nickname).encode('ascii'))
        client.close()
        print('{} has Disconnected .'.format(nickname) + ' ' + ctime())  

def receive():
    while True:
        client, address = server.accept()                          
        print("Connected with {}".format(str(address) + ' ' + ctime()))   

        client.send('NICK'.encode('ascii'))                       
        nickname = client.recv(1024).decode('ascii')                
        nicknames.append(nickname)
        clients.append(client)

        print("Name is {}".format(nickname))
        client.send('Connected to server!'.encode('ascii'))        

        thread = threading.Thread(target=handle, args=(client, nickname))   
        thread.start()                                             

receive()
