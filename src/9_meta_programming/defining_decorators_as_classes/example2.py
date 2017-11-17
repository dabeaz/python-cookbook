# Reformulation using closures and function attributes
from functools import wraps

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper

# Example

@profiled
def add(x, y):
    return x + y

class Spam:
    @profiled
    def bar(self, x):
        print(self, x)

if __name__ == '__main__':
    print(add(2,3))
    print(add(4,5))
    print('ncalls:', add.ncalls())

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print('ncalls:', Spam.bar.ncalls())
