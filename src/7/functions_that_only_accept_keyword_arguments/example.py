# examples of keyword-only argument functions

# A simple keyword-only argument
def recv(maxsize, *, block=True):
    print(maxsize, block)

recv(8192, block=False)        # Works
try:
    recv(8192, False)          # Fails
except TypeError as e:
    print(e)

# Adding keyword-only args to *args functions
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))
