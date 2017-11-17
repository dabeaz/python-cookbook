from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        if not hasattr(self.local, 'connections'):
            self.local.connections = []
        self.local.connections.append(sock)
        return sock
                
    def __exit__(self, exc_ty, exc_val, tb):
        self.local.connections.pop().close()

def test(conn):
    # Example use
    from functools import partial

    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))

    with conn as s1, conn as s2:
        s1.send(b'GET /downloads HTTP/1.0\r\n')
        s2.send(b'GET /index.html HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
        s2.send(b'\r\n')
        resp1 = b''.join(iter(partial(s1.recv, 8192), b''))
        resp2 = b''.join(iter(partial(s2.recv, 8192), b''))

    print('resp1 got {} bytes'.format(len(resp1)))
    print('resp2 got {} bytes'.format(len(resp2)))

if __name__ == '__main__':

    conn = LazyConnection(('www.python.org', 80))
    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t3 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


