import sample
print(sample.gcd(42, 8))
print(sample.divide(42, 8))
p1 = sample.Point(2, 3)
p2 = sample.Point(4, 5)
print(sample.distance(p1, p2))
print(p1.x)
print(p1.y)

import array
a = array.array('d', [1, 2, 3])
print(sample.avg(a))
