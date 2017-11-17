# example.py
#
# Examples of simple regular expression matching

import re

sep_line = "*" * 40
# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# (a) Find all matching dates
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))
print(sep_line)

# (b) Find all matching dates with capture groups
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
print(sep_line)

# (c) Iterative search
for m in datepat.finditer(text):
    print(m.groups())
