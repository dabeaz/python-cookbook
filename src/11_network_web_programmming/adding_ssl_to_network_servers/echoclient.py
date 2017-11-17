# echoclient.py
#
# An example of a client that connects to an SSL server
# and verifies its certificate

from socket import socket, AF_INET, SOCK_STREAM
import ssl

s = socket(AF_INET, SOCK_STREAM)

# Wrap with an SSL layer and require the server to present its certificate
ssl_s = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs='server_cert.pem',
                        )

ssl_s.connect(('localhost', 20000))

# Communicate with the server
ssl_s.send(b'Hello World!')
resp = ssl_s.recv(8192)
print('Got:', resp)

# Done
ssl_s.close()
