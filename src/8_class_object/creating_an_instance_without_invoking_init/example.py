from time import localtime

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Class method that bypasses __init__
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

d = Date.__new__(Date)
print(d)
print(hasattr(d,'year'))

data = { 
    'year' : 2012,
    'month' : 8,
    'day' : 29
}

d.__dict__.update(data)
print(d.year)
print(d.month)

d = Date.today()
print(d.year, d.month, d.day)

