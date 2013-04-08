from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
print('Got:', c.recv())
c.send(42)
print('Got:', c.recv())
c.send([1, 2, 3, 4, 5])
print('Got:', c.recv())

