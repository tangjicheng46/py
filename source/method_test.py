# 成员方法、类方法、静态方法

class A:
    count = 0

    def __init__(self, val, name):
        self.val = val
        self.name = name
        A.count += 1

    # 普通的成员方法
    def instance_print(self):
        print("name:", self.name, ", val: ", self.val)

    def not_ok_func():
        print(A.count)

    # 类方法
    @classmethod
    def count_num(cls):
        print("count: ", cls.count)

    # 静态方法
    @staticmethod
    def static_max(x, y):
        print(max(x, y))


a1 = A(1, "x")
A.count_num()
A.static_max(1, 2)
