from contextlib import contextmanager
from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]

# Example of using the subscribe() method
if __name__ == '__main__':
    # Example task (just for testing)
    class Task:
        def __init__(self, name):
            self.name = name
        def send(self, msg):
            print('{} got: {!r}'.format(self.name, msg))

    task_a = Task('A')
    task_b = Task('B')

    exc = get_exchange('spam')
    with exc.subscribe(task_a, task_b):
        exc.send('msg1')
        exc.send('msg2')

    exc.send('msg3')


