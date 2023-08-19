import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
	for client in clients:
		client.send(message)


def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except Exception as e:
			index = client.index(client)
			client.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} left this chat'.encode('utf-8'))
			nicknames.remove(nickname)
			break


def receive():
	while True:
		client, address = server.accept()
		print(f'Connected with {str(address)}')

		client.send('NICK'.encode('utf-8'))
		nickname = client.recv(1024).decode('utf-8')
		nicknames.append(client)

		print(f'Nickname of the client is {nickname}!')
		broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
		client.send('Connected to the server!'.encode('utf-8'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()


print('Serve is listining')
receive()

# cd C:\Users\jonat\OneDrive\Documentos\projetos\chat