# example.py
import sample

def foo():
    print('About to die')
    sample.die()

def bar():
    print('About to call the function that dies')
    foo()

def spam():
    print('About to call the function that calls the function that dies')
    bar()

if __name__ == '__main__':
    import faulthandler
    faulthandler.enable()
    spam()

