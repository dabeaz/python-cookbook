# example.py
#
# Example of splitting a string on multiple delimiters using a regex

import re


def print_sep_line():
    sep_line = "--" * 40
    print(sep_line)


line = 'asdf fjdk; afed, fjek,asdf,      foo'
print("line =" + line)
print_sep_line()

# (a) Splitting on space, comma, and semicolon
parts = re.split(r'[;,\s]\s*', line)
print("Splitting on space, comma, and semicolon")
print(parts)
print_sep_line()

# (b) Splitting with a capture group
print("Splitting with a capture group")
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
print_sep_line()

# (c) Rebuilding a string using fields above
print("Rebuilding a string using fields above")
values = fields[::2]  # 每隔1个元素
delimiters = fields[1::2]
delimiters.append('')
print('value =', values)
print('delimiters =', delimiters)
newline = ''.join(v + d for v, d in zip(values, delimiters))
print('newline =', newline)
print_sep_line()

# (d) Splitting using a non-capture group
print("Splitting using a non-capture group")
parts = re.split(r'(?:,|;|\s)\s*', line)
print(parts)
print_sep_line()
