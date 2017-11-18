# example.py
#
# Examples of variable interpolation

# Class for performing safe substitutions
class SafeSub(dict):
    def __missing__(self, key):
        return '{%s}' % key


s = '{name} has {n} messages.'

# (a) Simple substitution
name = 'Guido'
n = 37
a = 99
print("a", a)
print(s.format_map(vars()))
print("vars", vars())

# (b) Safe substitution with missing values
del n, a
print(s.format_map(SafeSub(vars())))
# ! print("a", a) #  NameError: name 'a' is not defined

# (c) Safe substitution + frame hack
n = 37
import sys


def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


print(sub('Hello {name}'))
print(sub('{name} has {n} messages'))
print(sub('Your favorite color is {color}'))
