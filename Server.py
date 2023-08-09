

import socket
import threading

# Connection Data  
#Port is confidential thing
host = '192.168.255.1'                                                 #IP of your host
port = 12345                                                       #Dont take reserved ports

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #Internet socket
server.bind((host, port))                                          #Server is binded to local host and a port  
server.listen()                                                    #Server is set to listining mode


from time import ctime

# Lists For Clients and Their Nicknames
clients = [] 
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message): 
    for client in clients:
        client.send(message)                                        #Getting all the clients and sending msg that new one joined to the admin

# Handling Messages From Clients
# ...

def handle(client):
    try:
        # ... (previous code)
        while True:
            # Broadcasting Messages
            message = client.recv(1024)
            if message.decode('ascii') == "quit":
                # ... (previous code)
                client.send('You have disconnected.'.encode('ascii'))
                client.close()
                print('{} has disconnected.'.format(nickname))  # Print disconnected message
                break
            else:
                broadcast(message)
    except:
        # Removing And Closing Clients
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        broadcast('{} Disconnect!'.format(nickname).encode('ascii'))
        nicknames.remove(nickname)
        client.close()
        print('{} has disconnected .'.format(nickname) +' '+ctime())  # Print error disconnect message

# ...
    


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()                          #In server IP wil login so different IP will login with same port on the server IP
        print("Connected with {}".format(str(address)+ ' '+ctime()))   

        #Getting nickname by asking --- code word sent the client and the client side accepts the encoded code which is NICK here and send backs the message that he can join
        #Request And Store Nickname

        client.send('NICK'.encode('ascii'))                        #Sending in encoded form 
        nickname = client.recv(1024).decode('ascii')                
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname  
        #pritning
        print("Name is {}".format(nickname))
        #broadcasting
        broadcast("{} joined!".format(nickname).encode('ascii'))   #So that every client will know new connection is joined
        client.send('Connected to server!'.encode('ascii'))        #Connected and can starting

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))   #This is because multiple client send multiple messages and so to avoid crashing we are handling with handler
        thread.start()                                             #To work with threads you need start method or run method

print("Server is started................,:) ")
receive()