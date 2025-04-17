import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))
while True:
    client.send(b'test')
    print(client.recv(1024))