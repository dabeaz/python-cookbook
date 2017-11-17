from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3])
print(s.keys())
print(s.get('foo'))
print(s.get('spam'))
s.delete('spam')
print(s.exists('spam'))
