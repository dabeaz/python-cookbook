# Example of using partial() with sorting a list of (x,y) coordinates

points = [ (1, 2), (3, 4), (5, 6), (7, 7) ]

import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4,3)
points.sort(key=partial(distance, pt))
print(points)
