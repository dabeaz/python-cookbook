import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n:int):
        '''
        Counts down
        '''
        while n > 0:
            n -= 1

    countdown(100000)
    print('Name:', countdown.__name__)
    print('Docstring:', repr(countdown.__doc__))
    print('Annotations:', countdown.__annotations__)
