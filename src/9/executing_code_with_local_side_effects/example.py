def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)      # --> 14

def test1():
    x = 0
    exec('x += 1')
    print(x)      # --> 0

def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)
 
def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

if __name__ == '__main__':
    print(':::: Running test()')
    test()

    print(':::: Running test1()')
    test1()

    print(':::: Running test2()')
    test2()

    print(':::: Running test3()')
    test3()

    print(':::: Running test4()')
    test4()

 

 

