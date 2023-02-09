# python中的内置函数，总是可用的，不需要import

class MyClass:
    def __init__(self, val: int) -> None:
        self.val = val

    def __abs__(self) -> int:
        return self.val + 100


x = MyClass(1)
print(abs(x))
