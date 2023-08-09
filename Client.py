# import socket
# import threading

# from time import ctime

# COLOR_RESET = '\033[0m'
# COLOR_BLUE = '\033[91m'  # Blue color
# COLOR_GREEN = '\033[92m'  # Green color

# HOST = '192.168.255.1'
# PORT = '12345'
# nickname = input("User Name: ")


# # Connecting To Server
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(f"Connecting to {HOST}:{PORT}...")
# client.connect(('192.168.255.1', 12345))                            #Instead of connecting, we'r binding to the host's port(Port Number is Confidential)


# def receive():
#     while True:
#         try:

#             message = client.recv(1024).decode('ascii')  

#             if message == 'NICK':                           
#                 client.send(nickname.encode('ascii'))    
#             else:
#                 print(COLOR_GREEN + message + COLOR_RESET)
#         except:
#             print(ctime() + ' ' + COLOR_BLUE + nickname + ' Disconnect!' + COLOR_RESET)
#             client.close()
#             break

# # Sending Messages To Server
# def write():
#     while True:
#         message = ctime() +' User '+ '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('ascii'))
#         if message.endswith(": quit"):
#             client.close()
#             break


# # Starting Threads For Listening And Writing
# receive_thread = threading.Thread(target=receive)
# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start() 


import socket
import threading

from time import ctime

COLOR_RESET = '\033[0m'
COLOR_BLUE = '\033[91m'  # Blue color
COLOR_GREEN = '\033[92m'  # Green color


HOST = '192.168.255.1'
PORT = '12345'

print('################## Welcome to the BigWorld ##################')
print('#################### Join to the Lobby ####################')
print('################## Enter your User Name ##################')
nickname = input("User Name: ")

print('##Select room##')
print('Select room 1 Enter 1')
print('Select room 2 Enter 2')
selectRoom = input('Select Room: ')


# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to {HOST}:{PORT}...")
client.connect(('192.168.255.1', 12345))                            #Instead of connecting, we'r binding to the host's port(Port Number is Confidential)


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
