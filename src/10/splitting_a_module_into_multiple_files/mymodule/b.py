# b.py

from .a import A

class B(A):
    def bar(self):
        print('B.bar')

