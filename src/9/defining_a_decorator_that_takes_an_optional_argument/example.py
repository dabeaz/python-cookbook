from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example use
@logged
def add(x, y):
    return x + y

@logged()
def sub(x, y):
    return x - y

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    add(2,3)
    sub(2,3)
    spam()

