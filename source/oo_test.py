# 继承层次，广度优先搜索

class A:
    def foo(self):
        print('called A.foo()')


class B(A):
    pass


class C(A):
    def foo(self):
        print('called C.foo()')


class D(B, C):
    pass


def foo(x):
    print(x.x)


class E:
    def __init__(self):
        self.x = 1


class F:
    global_var = 10

    def __init__(self):
        pass


if __name__ == '__main__':
    d = D()
    d.foo()
    foo(E())
    print(F.global_var)
