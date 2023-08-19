import socket
import threading

class Core:
    def __init__(self) -> None:
        self.host = '127.0.0.1'
        self.port = 55555

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        self.clients = []
        self.nicknames = []


    def broadcast(self, message):
        for client in self.clients:
            client.send(message)


    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast('{} left!'.format(nickname).encode('ascii'))
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)
            print("Nickname is {}".format(nickname))
            self.broadcast("{} joined!".format(nickname).encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()