import time
def test(func):
    start = time.time()
    nums = range(1000000)
    for n in range(100):
        r = func(nums)
    end = time.time()
    print(func.__name__, ':', end-start)

import math
def compute_roots_1(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

from math import sqrt
def compute_roots_2(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

def compute_roots_3(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

tests = [compute_roots_1, compute_roots_2, compute_roots_3]
for func in tests:
    test(func)
