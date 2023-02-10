import typing
from types import MethodType


class A:
    pass


def set1(self, age):
    self.age = age
    return self.age


def set2(self, age):
    self.age = age
    return self.age


class B:
    __slots__ = ('name', 'age')


if __name__ == "__main__":
    x1 = A()
    x1.age = 1

    A.score = 10
    x2 = A()
    print(x2.score)
    # print(x2.age)

    x1.set1 = MethodType(set1, x1)
    x1.set1(-1)
    print(x1.age)

    A.set2 = set2

    x1.set2(100)
    print(x1.age)

    y1 = B()
    # y1.xxx = 1
    # y1.xxx = MethodType(set1, y1)
    B.y = 1
    B.xxx = set1
