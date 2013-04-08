# Property example

class Person:
    first_name = property()
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

p = Person()
p.first_name = 'Dave'
print(p.first_name)
