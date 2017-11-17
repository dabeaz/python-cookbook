# Example of a HEAD request

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified =	resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']

print(status)
print(last_modified)
print(content_type)
print(content_length)
