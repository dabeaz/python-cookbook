# A proxy class that wraps around another object, but
# exposes its public attributes

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

if __name__ == '__main__':
    class Spam:
        def __init__(self, x):
            self.x = x
        def bar(self, y):
            print('Spam.bar:', self.x, y)

    # Create an instance
    s = Spam(2)

    # Create a proxy around it
    p = Proxy(s)

    # Access the proxy
    print(p.x)     # Outputs 2
    p.bar(3)       # Outputs "Spam.bar: 2 3"
    p.x = 37       # Changes s.x to 37
