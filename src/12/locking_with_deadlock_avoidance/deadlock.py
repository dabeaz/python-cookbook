import threading
from collections import defaultdict
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    if not locks:
        return
    # Sort locks by object identifier
    locks = sorted(locks, key=id)

    # Make sure lock order of previously acquired locks is not violated
    if hasattr(_local, 'acquired'):
        acquired = _local.acquired
    else:
        _local.acquired = acquired = defaultdict(int)
    # We delete entries at 0 to avoid holding onto references.
    assert all(val > 0 for val in acquired.values())
    # Strict inequality: lock could already be acquired if using RLocks
    if acquired and max(id(lock) for lock in acquired) > id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    try:
        for lock in locks:
            lock.acquire()
            acquired[lock] += 1
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
            acquired[lock] -= 1
            if acquired[lock] == 0:
              del acquired[lock]
