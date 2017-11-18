# example.py
#
# Example of combining text via generators
word_sep = " "


def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


# (a) Simple join operator
text = word_sep.join(sample())
print(text)

# (b) Redirection of parts to I/O
import sys

for part in sample():
    sys.stdout.write(part + word_sep)
sys.stdout.write('\n')


# (c) Combination of parts into buffers and larger I/O operations
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield word_sep.join(parts)


for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')
