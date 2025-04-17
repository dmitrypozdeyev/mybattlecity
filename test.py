import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 1234))

s.listen(1)

print('Waiting for connection...')

conn, addr = s.accept()

print('Connected by', addr)

data = conn.recv(1024)

print(data)