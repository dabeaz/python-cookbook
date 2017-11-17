# Example of managed attributes via properties

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

if __name__ == '__main__':
   a = Person('Guido')
   print(a.first_name)
   a.first_name = 'Dave'
   print(a.first_name)
   try:
       a.first_name = 42
   except TypeError as e:
       print(e)
