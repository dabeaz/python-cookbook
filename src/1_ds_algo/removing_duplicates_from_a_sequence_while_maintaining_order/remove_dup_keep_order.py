# example2.py
#
# Remove duplicate entries from a sequence while keeping order
from typing import Set


def dedupe(items, key=None) -> Set:
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15}
    ]
    print("original list", a)
    de_duplicate = dedupe(a, key=lambda a: (a['x'], a['y']))
    print("deduplicate(generator): ", de_duplicate)
    print("remove duplicate", list(dedupe(a, key=lambda a: (a['x'], a['y']))))
