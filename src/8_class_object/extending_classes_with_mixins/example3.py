# Class decorator alternative to mixins

def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting %s' % key)
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting %s = %r' % (key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting %s' % key)
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls

@LoggedMapping
class LoggedDict(dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']
