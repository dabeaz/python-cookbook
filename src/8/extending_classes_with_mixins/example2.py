class RestrictKeysMixin:
    # there is an underscore not present which is added in it 
    def __init__(self, _restrict_key_type, *args, **kwargs):
        self.__restrict_key_type = _restrict_key_type
        super().__init__(*args, **kwargs)
    
    def __setitem__(self, key, value):
        if not isinstance(key, self.__restrict_key_type):
            raise TypeError(f'Keys must be of type {self.__restrict_key_type.__name__}')
        super().__setitem__(key, value)

# Example

class RDict(RestrictKeysMixin, dict):
    def __init__(self, *args, _restrict_key_type=None, **kwargs):
        if _restrict_key_type is None:
            raise ValueError("_restrict_key_type must be specified")
        super().__init__(_restrict_key_type=_restrict_key_type, *args, **kwargs)

# Usage
try:
    d = RDict()  # This will raise a ValueError because _restrict_key_type is not specified
except ValueError as e:
    print(e)

e = RDict([('name', 'Dave'), ('n', 37)], _restrict_key_type=str)
f = RDict(name='Dave', n=37, _restrict_key_type=str)
print(f)

try:
    f[42] = 10  # This will raise a TypeError because the key is not of type str
except TypeError as e:
    print(e)
