# Example of accessing variables inside a closure
class Sample:
    def __init__(self):
        self._n = 0

    def func(self):
        print(f'n={self._n}')

    def get_n(self):
        return self._n

    def set_n(self, value):
        self._n = value

if __name__ == '__main__':
    s = Sample()
    s.func()
    s.set_n(10)
    s.func()
    print(s.get_n())