# Example of accessing variables inside a closure

def sample():
    n = 0           
    # Closure function
    def func():
        print('n=', n)
    
    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

if __name__ == '__main__':
    f = sample()
    f()
    n= 0
    f.set_n(10)
    f()
    print(f.get_n())
