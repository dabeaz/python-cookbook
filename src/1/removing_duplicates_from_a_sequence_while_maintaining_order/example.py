# example.py
#
# Remove duplicate entries from a sequence while keeping order

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(a)
    print(list(dedupe(a)))
