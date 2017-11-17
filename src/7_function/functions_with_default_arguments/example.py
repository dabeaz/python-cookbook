# Examples of a function with default arguments

# (a) Dangers of using a mutable default argument

def spam(b=[]):
    return b

a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)       #  Carefully observe result
print('-'*10)

# (b) Better alternative for mutable defaults
def spam(b=None):
    if b is None:
        b = []
    return b

a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)
print('-'*10)

# (c) Example of testing if an argument was supplied or not

_no_value = object()
def spam(b=_no_value):
    if b is _no_value:
        print("No b value supplied")
    else:
        print("b=", b)

spam()
spam(None)
spam(0)
spam([])
