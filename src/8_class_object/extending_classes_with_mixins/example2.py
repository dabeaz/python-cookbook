class RestrictKeysMixin:
    def __init__(self, *args, _restrict_key_type, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)
    
    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError('Keys must be ' + str(self.__restrict_key_type))
        super().__setitem__(key, value)

# Example

class RDict(RestrictKeysMixin, dict):
    pass
 
d = RDict(_restrict_key_type=str)
e = RDict([('name','Dave'), ('n',37)], _restrict_key_type=str)
f = RDict(name='Dave', n=37, _restrict_key_type=str)
print(f)
try:
    f[42] = 10
except TypeError as e:
    print(e)
