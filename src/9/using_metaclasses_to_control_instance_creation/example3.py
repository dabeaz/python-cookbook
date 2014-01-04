# example3.py
#
# Cached instances

import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        try:
            return self.__cache[args]
        except KeyError:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj
        
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

if __name__ == '__main__':
    a = Spam('foo')
    b = Spam('bar')
    print('a is b:', a is b)
    c = Spam('foo')
    print('a is c:', a is c)


