import time
import threading
from deadlock import acquire

x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print("Thread-1")
            time.sleep(1)

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print("Thread-2")
            time.sleep(1)

input('This program runs forever. Press [return] to start, Ctrl-C to exit')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

while True:
    time.sleep(1)
