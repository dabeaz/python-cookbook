from contextlib import contextmanager

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working

# Example
if __name__ == '__main__':
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)
    print(items)
    try:
        with list_transaction(items) as working:
            working.append(6)
            working.append(7)
            raise RuntimeError('oops')
    except RuntimeError as e:
        print(e)

    print(items)
    
