import sample
p1 = sample.Point(2, 3)
p2 = sample.Point(4, 5)
print(p1)
print(p2)
print(sample.distance(p1, p2))
del p1
del p2
print('Done')
