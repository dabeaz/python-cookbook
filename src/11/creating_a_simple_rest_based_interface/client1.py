from urllib.request import urlopen

u = urlopen('http://localhost:8080/hello?name=Guido')
print(u.read().decode('utf-8'))

u = urlopen('http://localhost:8080/localtime')
print(u.read().decode('utf-8'))
