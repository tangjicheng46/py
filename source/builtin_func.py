# python中的内置函数，总是可用的，不需要import

class MyClass:
    def __init__(self, val: int) -> None:
        self.val = val

    def __abs__(self) -> int:
        return self.val + 100


x = MyClass(1)
print(abs(x))


class A:
    @staticmethod
    def func():
        print("A.func()")

    @classmethod
    def func2(cls):
        print("A.func2")

    def func3():
        print("A.func3")


A.func()
A().func()
A.func2()
A().func2()
A.func3()
# A().func3()  # 用对象调用，会默认传入参数self，与func3的函数参数列表不相符，出错
