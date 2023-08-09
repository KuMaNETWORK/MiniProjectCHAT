from socket import *

HOST = '10.60.131.140'
PORT = 5000
BUFFER_SIZE = 4096
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
messageFromServer = bytes.decode(server.recv(BUFFER_SIZE))
print(messageFromServer)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)

def big1():
    
    while True:
        print('Welcome to the room 1')
        receiveMessage = bytes.decode(server.recv(BUFFER_SIZE))
        if not receiveMessage:
            print('Server disconnected')
            break
        print(receiveMessage)
        sendMessage = input('Enter your message: ')
        if not sendMessage:
            print('Server disconnected')
            break

        if sendMessage.lower() == str('leave'):
            print('Server disconnected')
            break
        
        server.send(str.encode(sendMessage))

def big2():
    print('Welcome to the room 2')
    while True:
        receiveMessage = bytes.decode(server.recv(BUFFER_SIZE))
        if not receiveMessage:
            print('Server disconnected')
            break
        print(receiveMessage)
        sendMessage = input('Enter your message: ')
        if not sendMessage:
            print('Server disconnected')
            break

        if sendMessage.lower() == str('leave'):
            print('Server disconnected')
            break
        
        server.send(str.encode(sendMessage))

print('Select Room')
print('Room 1 Enter 1')
print('Room 2 Enter 2')

room = input('Enter room: ')
if room == '1':
    big1()
if room == '2':
    big2()
else :
    pass

server.close()