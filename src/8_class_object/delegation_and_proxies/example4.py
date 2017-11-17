class A:
    def spam(self):
        print('A.spam')

    def foo(self):
        print('A.foo')

class B:
    def __init__(self):
        self._a = A()

    def spam(self):
        print('B.spam')
        self._a.spam()     # Similar to super()

    def __getattr__(self, name):
        return getattr(self._a, name)

if __name__ == '__main__':
    b = B()
    b.spam()
    b.foo()
