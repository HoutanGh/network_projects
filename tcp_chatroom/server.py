import threading
import socket

host = '127.0.0.1' # localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, TCP
server.bind((host, port))
server.listen() # listen for incoming connections

clients_list = []
nicknames = []

# broadcast method
def broadcast(message):
    for client in clients_list:
        client.send(message)

# handle method
def handle(client):
    while True:
        try:
            message = client.recv(1024) # receive message from client 1024 bytes
            broadcast(message) # broadcast message to all clients
        except:
            index = clients_list.index(client)  
            clients_list.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

# receive method
def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('NICK'.encode('ascii')) # if client receives 'NICK' it will send its nickname
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients_list.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server is listening...')
receive()