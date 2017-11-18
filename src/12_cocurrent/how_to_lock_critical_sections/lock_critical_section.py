import threading

class SharedCounter:
    '''
    A counter object that can be shared by multiple threads.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self,delta=1):
        """Increment the counter with locking"""
        with self._value_lock:
             self._value += delta

    def decr(self,delta=1):
        '''
        Decrement the counter with locking
        '''
        with self._value_lock:
             self._value -= delta

def test(c):
    for n in range(1000000):
        c.incr()
    for n in range(1000000):
        c.decr()

if __name__ == '__main__':
    c = SharedCounter()
    t1 = threading.Thread(target=test, args=(c,))
    t2 = threading.Thread(target=test, args=(c,))
    t3 = threading.Thread(target=test, args=(c,))
    t1.start()
    t2.start()
    t3.start()
    print('Running test')
    t1.join()
    t2.join()
    t3.join()
    
    assert c._value == 0
    print('Looks good!')
