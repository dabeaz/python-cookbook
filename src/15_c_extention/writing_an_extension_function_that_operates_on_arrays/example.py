import array
from sample import avg

print(avg(array.array('d',[1,2,3])))
try:
    import numpy
    print(avg(numpy.array([1., 2., 3.])))
except ImportError:
    pass

