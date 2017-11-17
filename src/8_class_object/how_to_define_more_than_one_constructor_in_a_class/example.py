import time

class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

if __name__ == '__main__':
    a = Date(2012, 12, 21)
    b = Date.today()
    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)

    class NewDate(Date):
        pass

    c = Date.today()
    d = NewDate.today()
    print('Should be Date instance:', Date)
    print('Should be NewDate instance:', NewDate)
