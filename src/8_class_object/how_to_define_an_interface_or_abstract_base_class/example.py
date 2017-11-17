# Defining a simple abstract base class

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

# Example implementation
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('reading')
    def write(self, data):
        print('writing')

# Example of type checking
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    print('serializing')

# Examples
if __name__ == '__main__':
    # Attempt to instantiate ABC directly (doesn't work)
    try:
        a = IStream()
    except TypeError as e:
        print(e)

    # Instantiation of a concrete implementation
    a = SocketStream()
    a.read()
    a.write('data')

    # Passing to type-check function
    serialize(None, a)

    # Attempt to pass a file-like object to serialize (fails)
    import sys

    try:
        serialize(None, sys.stdout)
    except TypeError as e:
        print(e)

    # Register file streams and retry
    import io
    IStream.register(io.IOBase)

    serialize(None, sys.stdout)



