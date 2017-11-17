import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
      
class Spam:
    def __init__(self, name):
        self.name = name

Spam.manager = CachedSpamManager()

def get_spam(name):
    return Spam.manager.get_spam(name)

if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    print('a is b:', a is b)
    c = get_spam('foo')
    print('a is c:', a is c)
