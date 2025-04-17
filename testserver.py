import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1234))
server.listen(1)
print('Ожидание соединения')
client, addr = server.accept()
while True:
    print(client.recv(1024))
    client.send(b'hello from server')