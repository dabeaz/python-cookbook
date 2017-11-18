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


if __name__ == '__main__':
    d = Date.__new__(Date)
    print("date", d)
    print("hasattr(d,'year'): ", hasattr(d, 'year'))

    data = {'year': 2012, 'month': 8, 'day': 29}
    d.__dict__.update(data)
    print("year", d.year)
    print("month", d.month)

    d = Date.today()
    print("year", d.year, "month", d.month, "day", d.day)
