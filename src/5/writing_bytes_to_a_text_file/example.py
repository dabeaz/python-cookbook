# Example of writing raw bytes on a file opened in text mode

import sys

# A byte string
data = b'Hello World\n'

# Write onto the buffer attribute (bypassing text encoding)
sys.stdout.buffer.write(data)
