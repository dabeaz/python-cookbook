# example.py
#
# Example of unicode normalization

# Two strings
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

# (a) Print them out (usually looks identical)
print(s1)
print(s2)

# (b) Examine equality and length
print('s1 == s2', s1 == s2)
print(len(s1), len(s2))

# (c) Normalize and try the same experiment
import unicodedata

n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)

print('n_s1 == n_s2', n_s1 == n_s2)
print(len(n_s1), len(n_s2))

# (d) Example of normalizing to a decomposed form and stripping accents
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
