# 类似于C/C++的struct
from dataclasses import dataclass


@dataclass
class A:
    name: str
    x_name: str = 'xxx'
    val: int = 0


a = A(val=1, name="v")
print(a.val)
print(a.x_name)
