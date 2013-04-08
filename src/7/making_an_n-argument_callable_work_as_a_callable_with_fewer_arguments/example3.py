# Using partial to supply extra arguments to a class constructor
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

if __name__ == '__main__':
    from functools import partial
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    print('Echo server running on port 15000')
    serv.serve_forever()
