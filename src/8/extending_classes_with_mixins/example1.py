class LoggedMappingMixin:
    '''
    Add logging to get/set/delete operations for debugging.
    '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)
    
class SetOnceMappingMixin:
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class StringKeysMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


# Examples

print('# ---- LoggedDict Example')

class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']

print('# ---- SetOnceDefaultDict Example')

from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass
 
d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
try:
    d['x'] = 23
except KeyError as e:
    print(e)

print('# ---- StringOrderedDict Example')
from collections import OrderedDict

class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
try:
    d[42] = 10
except TypeError as e:
    print(e)

try:
    d['x'] = 42
except KeyError as e:
    print(e)
