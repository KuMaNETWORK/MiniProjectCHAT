# import socket
# import threading
# from time import ctime

# host = '192.168.255.1'                                                 
# port = 12345                                                       
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# server.bind((host, port))                                          
# server.listen()                                                   


# clients = [] 
# nicknames = []

# def broadcast(message): 
#     for client in clients:
#         client.send(message)                                       

 
# def handle(client):
#     try:
#         while True:
#             message = client.recv(1024)
#             if message.decode('ascii') == "quit":
#                 client.send('You have disconnected.'.encode('ascii'))
#                 client.close()
#                 print('{} has disconnected.'.format(nickname))
#                 break
#             else:
#                 broadcast(message)
#     except:
#         index = clients.index(client)
#         clients.remove(client)
#         nickname = nicknames[index]
#         broadcast('{} Disconnect!'.format(nickname).encode('ascii'))
#         nicknames.remove(nickname)
#         client.close()
#         print('{} has Disconnected .'.format(nickname) +' '+ctime())  


# def receive():
#     while True:
#         client, address = server.accept()                          
#         print("Connected with {}".format(str(address)+ ' '+ctime()))   

#         client.send('NICK'.encode('ascii'))                       
#         nickname = client.recv(1024).decode('ascii')                
#         nicknames.append(nickname)
#         clients.append(client)


#         print("Name is {}".format(nickname))
#         #broadcasting
#         broadcast("{} joined!".format(nickname).encode('ascii'))   
#         client.send('Connected to server!'.encode('ascii'))        

#         thread = threading.Thread(target=handle, args=(client,))   
#         thread.start()                                             

# print("Server is started..............,:) ")
# receive()




def room1():
    import socket
    import threading
    from time import ctime

    host = '192.168.255.1'                                                 
    port = 12345                                                       
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
    server.bind((host, port))                                          
    server.listen()                                                   
    print("Welcome to Room 1")

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
            #broadcasting
            broadcast("{} joined!".format(nickname).encode('ascii'))   
            client.send('Connected to server!'.encode('ascii'))        

            thread = threading.Thread(target=handle, args=(client,))   
            thread.start()                                             

    print("Server is started..............,:) ")
    receive()



def room2():
    import socket
    import threading
    from time import ctime
    
    print("Welcome to Room 2")

    host = '192.168.255.1'                                                 
    port = 12345                                                       
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
            #broadcasting
            broadcast("{} joined!".format(nickname).encode('ascii'))   
            client.send('Connected to server!'.encode('ascii'))        

            thread = threading.Thread(target=handle, args=(client,))   
            thread.start()                                             

    print("Server is started..............,:) ")
    receive()

import socket
import threading
from time import ctime

host = '192.168.255.1'                                                 
port = 12345                                                       
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
        #broadcasting
        broadcast("{} joined!".format(nickname).encode('ascii'))   
        client.send('Connected to server!'.encode('ascii'))        

        thread = threading.Thread(target=handle, args=(client,))   
        thread.start()                                             

print("Server is started..............,:) ")
receive()

if __name__ == "__main__":
    selectRoom = input("Select room 1: ")
    if selectRoom == '1':
        room1()
    if selectRoom == '2':
        room2()


