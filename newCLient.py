import socket
import threading

from time import ctime

COLOR_RESET = '\033[0m'
COLOR_BLUE = '\033[91m'  # Blue color
COLOR_GREEN = '\033[92m'  # Green color

HOST = '192.168.255.1'
PORT = 8000
nickname = input("User Name: ")


# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to {HOST}:{PORT}...")
client.connect(('192.168.255.1', 8000))                            #Instead of connecting, we'r binding to the host's port(Port Number is Confidential)


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

# Sending Messages To Server
def write():
    while True:
        message = ctime() +' User '+ '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
        if message.endswith(": quit"):
            client.close()
            break


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start() 
