from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
		
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

if __name__ == '__main__':
    from functools import partial

    c = LazyConnection(('www.python.org', 80))
    # Connection closed
    with c as s:
        # c.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        # c.__exit__() executes: connection closed

    print('Got %d bytes' % len(resp))
