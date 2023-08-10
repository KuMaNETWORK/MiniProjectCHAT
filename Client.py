import socket
import threading

from time import ctime

COLOR_RESET = '\033[0m'
COLOR_BLUE = '\033[91m'  # Blue color
COLOR_GREEN = '\033[92m'  # Green color

HOST = '10.60.131.140'
PORT = 12345

print('################## Welcome to the BigWorld ##################')
print('#################### Join to the Lobby ####################')
print('################## Enter your User Name ##################')
nickname = input("User Name: ")

# Define the server information for each room
ROOM_SERVERS = {
    '1': ('10.60.131.140', 1000),
    '2': ('10.60.131.140', 2000),
    '3': ('10.60.131.140', 3000),
    '4': ('10.60.131.140', 4000),
    '5': ('10.60.131.140', 5000),
    '6': ('10.60.131.140', 6000),
    'big': ('10.60.131.140', 10000),
    'bee': ('10.60.131.140', 20000),

}

def select_room():
    global client
    while True:
        print('##Select room##')
        print('Enter 1 Select room 1 ')
        print('Enter 2 Select room 2 ')
        print('Enter 1 Select room 3 ')
        print('Enter 2 Select room 4 ')
        print('Enter 1 Select room 5 ')
        print('Enter 2 Select room 6 ')
        print('Enter quit Disconnect Form Lobby ')
        print('Enter create for Create Room')
        selectRoom = input('Select Room: ')
        if selectRoom == 'quit':
            client.close()
            break
        if selectRoom.lower() == 'create':
            create_room()
            continue
        room_server = ROOM_SERVERS.get(selectRoom)
        if room_server is None:
            print('Invalid room selection.')
        else:
            server_host, server_port = room_server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"Connecting to {server_host}:{server_port}...")
            client.connect((server_host, server_port))
            print(f"Connected to Room {selectRoom}!")
            break

def create_room():
    room_name = input("Enter room name: ")
    room_port = int(input("Enter room port: "))

    server_code = f'''
import socket
import threading
from time import ctime

host = '10.60.131.140'                                                 
port = {room_port}                                                      
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
                print('{{}} has disconnected.'.format(nickname))
                break
            else:
                broadcast(message)
    except:
        index = clients.index(client)
        clients.remove(client)
        nicknames.pop(index)
        broadcast('{{}} Disconnect!'.format(nickname).encode('ascii'))
        client.close()
        print('{{}} has Disconnected .'.format(nickname) + ' ' + ctime())  

def receive():
    while True:
        client, address = server.accept()                          
        print("Connected with {{}}".format(str(address) + ' ' + ctime()))   

        client.send('NICK'.encode('ascii'))                       
        nickname = client.recv(1024).decode('ascii')                
        nicknames.append(nickname)
        clients.append(client)

        print("Name is {{}}".format(nickname))
        client.send('Connected to server!'.encode('ascii'))        

        thread = threading.Thread(target=handle, args=(client, nickname))   
        thread.start()                                             

receive()
    '''

    with open(f'Server_{room_name}.py', 'w') as f:
        f.write(server_code)

select_room()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')

            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(COLOR_GREEN + message + COLOR_RESET)
        except:
            print(ctime() + ' ' + COLOR_BLUE + nickname + ' Disconnect!' + COLOR_RESET)
            client.close()
            break

def write():
    while True:
        message = ctime() + ' User ' + '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
        if message.endswith(": leave"):
            client.close()
            select_room()
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
