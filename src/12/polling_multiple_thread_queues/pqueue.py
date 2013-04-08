import queue
import socket
import os

class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # Create a pair of connected sockets        
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super().get()

# Example code that performs polling:

if __name__ == '__main__':
    import select
    import threading
    import time

    def consumer(queues):
        '''
        Consumer that reads data on multiple queues simultaneously
        '''
        while True:
            can_read, _, _ = select.select(queues,[],[])
            for r in can_read:
                item = r.get()
                print('Got:', item)

    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()
    t = threading.Thread(target=consumer, args=([q1,q2,q3],))
    t.daemon = True
    t.start()

    # Feed data to the queues
    q1.put(1)
    q2.put(10)
    q3.put('hello')
    q2.put(15)

    # Give thread time to run
    time.sleep(1)
