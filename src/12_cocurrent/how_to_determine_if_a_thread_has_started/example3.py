import threading
import time

# Worker thread
def worker(n, sema):
    # Wait to be signalled
    sema.acquire()
    # Do some work
    print("Working", n)

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.daemon=True
    t.start()

print('About to release first worker')
time.sleep(5)
sema.release()
time.sleep(1)
print('About to release second worker')
time.sleep(5)
sema.release()
time.sleep(1)
print('Goodbye')
