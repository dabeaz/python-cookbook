# Simple example

class Spam:
    def __init__(self, name):
        self.name = name

# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    print('a is b:', a is b)
    c = get_spam('foo')
    print('a is c:', a is c)


