class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


if __name__ == '__main__':
    b = B()
    print(b.x, b.y)  # 0 1
