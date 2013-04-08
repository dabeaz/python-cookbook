# Example involving new and some of its problems

import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Initializing Spam')
        self.name = name

if __name__ == '__main__':
    print("This should print 'Initializing Spam' twice")
    s = Spam('Dave')
    t = Spam('Dave')
    print(s is t)

