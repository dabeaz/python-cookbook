import time


class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def end(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()


if __name__ == '__main__':

    def countdown(n):
        while n > 0:
            n -= 1

    # (a) traditional way: elapsed = end - start
    print("(a) traditional way: elapsed = end - start")
    t = Timer()
    t.start()
    countdown(20000000)
    t.end()
    print(t.elapsed)

    # (b) context manager
    print("(b) context manager")
    with t:
        countdown(20000000)
    print(t.elapsed)
