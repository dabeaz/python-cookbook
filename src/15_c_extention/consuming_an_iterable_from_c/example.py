import sample

sample.consume_iterable([1,2,3,4])

def countdown(n):
    while n > 0:
        yield n
        n -= 1

sample.consume_iterable(countdown(10))
