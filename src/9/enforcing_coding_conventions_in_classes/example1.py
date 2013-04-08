# A metaclass that disallows mixed case identifier names

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):      # Ok
        pass

print('**** About to generate a TypeError')
class B(Root):
    def fooBar(self):       # TypeError
        pass
