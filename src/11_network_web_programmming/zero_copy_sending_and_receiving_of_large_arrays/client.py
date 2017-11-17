from zerocopy import recv_into
from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(('localhost', 25000))

import numpy
a = numpy.zeros(shape=50000000, dtype=float)
print(a[0:10])
recv_into(a, c)
print(a[0:10])
print(a[-10:])
