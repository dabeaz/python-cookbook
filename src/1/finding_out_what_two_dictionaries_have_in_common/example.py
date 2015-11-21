# example.py
#
# Find out what two dictionaries have in common

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}


common_keys = list(set(a.keys()) & set(b.keys()))
dic_keys = list(set(a.keys()) - set(b.keys()))
common_key_pairs = list(set(a.items()) & set(b.items()))

print('Common keys:', common_keys)
print('Keys in a not in b:', dic_keys)
print('(key,value) pairs in common:', common_key_pairs)

