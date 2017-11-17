from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))

s.send(b'Hello\n')
resp = s.recv(8192)
print('Response:', resp)
s.close()

