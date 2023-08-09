import socket
import threading

from time import ctime

COLOR_RESET = '\033[0m'
COLOR_BLUE = '\033[91m'  # Blue color
COLOR_GREEN = '\033[92m'  # Green color

HOST = '192.168.255.1'
PORT = 12345

print('################## Welcome to the BigWorld ##################')
print('#################### Join to the Lobby ####################')
print('################## Enter your User Name ##################')
nickname = input("User Name: ")

# Define the server information for each room
ROOM_SERVERS = {
    '1': ('192.168.255.1', 1000),
    '2': ('192.168.255.1', 2000),
    '3': ('192.168.255.1', 3000)
}

def select_room():
    global client
    while True:
        print('##Select room##')
        print('Enter 1 Select room 1 ')
        print('Enter 2 Select room 2 ')
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

host = '192.168.255.1'
port = {room_port}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

# ... (โค้ดที่เหลือจาก Server1.py)

print("Server {room_name} is started..............,:)")
receive()
    '''
    with open(f'Server{room_name}.py', 'w') as f:
        f.write(server_code)
    
    print(f"Server {room_name} has been created.")

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
