class A:
    l = [1, 2, 3, 4]

    def __init__(self):
        self.val = 0


a1 = A()
a1.l[0] = -1
b1 = A()
print(b1.l[0])
