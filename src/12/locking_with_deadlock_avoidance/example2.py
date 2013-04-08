import threading
import time
from deadlock import acquire


x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print("Thread-1")
                time.sleep(1)

def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print("Thread-2")
                time.sleep(1)

input('This program crashes with an exception. Press [return] to start')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

time.sleep(5)

