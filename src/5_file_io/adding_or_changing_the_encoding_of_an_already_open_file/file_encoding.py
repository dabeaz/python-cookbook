# Example of adding a text encoding to existing file-like object

import urllib.request
import io

import time

start = time.time()
# u = urllib.request.urlopen('http://www.python.org')
u = urllib.request.urlopen('http://httpbin.org/ip')
u = urllib.request.urlopen('http://www.baidu.com')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

print(text)
end = time.time()
exec_time = end - start

print("%d seconds used" % exec_time)
