# Examples of different ways to filter data

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print("mylist: ", mylist)
# All positive values
pos = [n for n in mylist if n > 0]
print("All positive values: ", pos)

# All negative values
neg = [n for n in mylist if n < 0]
print("All negative values", neg)

# Negative values clipped to 0
neg_clip = [n if n > 0 else 0 for n in mylist]
print("Negative values clipped to 0", neg_clip)

# Positive values clipped to 0
pos_clip = [n if n < 0 else 0 for n in mylist]
print("Positive values clipped to 0:", pos_clip)

# Compressing example
print("Compressing example")
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
compressed = compress(addresses, more5)
print("compressed:", compressed)
print("compressed type:", type(compressed))
a = list(compress(addresses, more5))
print(a)
