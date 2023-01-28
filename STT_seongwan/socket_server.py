'''
    Server program to receive speech text from each users, and
    create a whole trascript and user-specific transcript.
'''

import socket
from _thread import *

# Socket connection parameters
HOST = '192.168.1.10'
PORT = 9999

client_sockets = []
whole_transcript = []
client_transcript = {}

# Dedicated thread function for receiving speech text from each users
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    # Repeat until user disconnects
    while True:

        try:
            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            text_data, username = data.decode().split(';')

            print('>> Received from : ' + username," data : ", text_data)
            whole_transcript.append({'username':username, 'data' : text_data})
            print('whole_transcript : ',whole_transcript)
            for i in whole_transcript :
                print(i['username'])
                print(i['data'])


        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets :
        client_sockets.remove(client_socket)
        print('remove client list : ',len(client_sockets))

    client_socket.close()


def main():
    print('>> Server Start')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    try:
        while True:
            print('>> Waiting for connection...')

            client_socket, addr = server_socket.accept()
            client_sockets.append(client_socket)
            client_transcript[addr[0]] = [] # addr[0] = 192.168.1.10
            start_new_thread(threaded, (client_socket, addr))
            print("Number of clients: ", len(client_sockets))
            
    except Exception as e :
        print (e)

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()