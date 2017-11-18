# Example of calling methods by name

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(4, 3)

# Method 1 : Use getattr
d = getattr(p, 'distance')(0, 0)  # Calls p.distance(0, 0)
print("distance", d)

# Method 2: Use methodcaller
import operator

d = operator.methodcaller('distance', 0, 0)(p)
print("distance", d)
print()
# Application in sorting
points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]

# Sort by distance from origin (0, 0)
print("Sort by distance:")
points.sort(key=operator.methodcaller('distance', 0, 0))
for p in points:
    print(p)
