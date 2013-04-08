class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)    # Call original __setattr__
        else:
            setattr(self._obj, name, value)

if __name__ == '__main__':
    class A:
        def __init__(self, x):
            self.x = x
        def spam(self):
            print('A.spam')

    a = A(42)
    p = Proxy(a)
    print(p.x)
    print(p.spam())
    p.x = 37
    print('Should be 37:', p.x)
    print('Should be 37:', a.x)

    
