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
        print('Select room 1 Enter 1')
        print('Select room 2 Enter 2')
        selectRoom = input('Select Room: ')
        
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
        if message.endswith(": quit"):
            client.close()
            select_room()
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
