# example.py
#
# Example of combining dicts into a chainmap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# (a) Simple example of combining
from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])      # Outputs 1  (from a)
print(c['y'])      # Outputs 2  (from b)
print(c['z'])      # Outputs 3  (from a)

# Output some common values
print('len(c):', len(c))
print('c.keys():', list(c.keys()))
print('c.values():', list(c.values()))

# Modify some values
c['z'] = 10
c['w'] = 40
del c['x']
print("a:", a)


# Example of stacking mappings (like scopes)
values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values)
print(values['x'])

