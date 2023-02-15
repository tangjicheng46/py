class A:
    a = 1
    b = 2

    def func(self):
        print("before:", self.a)
        A.a = 3
        print("after:", self.a)


a1 = A()
print(a1.a)
a1.func()
print(A.a)
a1.a = -1
A.a = 2
b1 = A()
print(b1.a)
print(a1.a)
