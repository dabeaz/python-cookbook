# example1.py
#
# Not allowing direct instantiation

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

if __name__ == '__main__':
    try:
        s = Spam()
    except TypeError as e:
        print(e)

    Spam.grok(42)
