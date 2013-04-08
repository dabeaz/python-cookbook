class Structure:
    # Class variable that specifies expected fields
    _fields= []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        
# Example class definitions
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x','y']

    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s.name, s.shares, s.price)

    p = Point(2,3)
    print(p.x, p.y)

    c = Circle(4.5)
    print(c.radius)

    try:
        s2 = Stock('ACME', 50)
    except TypeError as e:
        print(e)
