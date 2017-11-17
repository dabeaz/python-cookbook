from postimport import when_imported
from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper

# Example
@when_imported('math')
def add_logging(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)

if __name__ == '__main__':
    import math
    print(math.cos(2))
    print(math.sin(2))

