from socketserver import StreamRequestHandler, TCPServer
import socket

class EchoHandler(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        try:
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out!')

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    print('Echo server running on port 20000')
    serv.serve_forever()
