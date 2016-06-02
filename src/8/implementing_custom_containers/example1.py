# Example of a custom container

import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)

if __name__ == '__main__':
   items = SortedItems([5, 1, 3])
   print(list(items))
   print(items[0])
   print(items[-1])
   items.add(2)
   print(list(items))
   items.add(-10)
   print(list(items))
   print(items[1:4])
   print(3 in items)
   print(len(items))
   for n in items:
       print(n)
