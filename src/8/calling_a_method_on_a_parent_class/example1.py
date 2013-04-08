class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()      # Call parent spam()

if __name__ == '__main__':
    b = B()
    b.spam()
