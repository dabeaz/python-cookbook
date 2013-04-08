from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 16000))
s.send(b'Hello\n')
print('Got:', s.recv(8192))
s.close()
