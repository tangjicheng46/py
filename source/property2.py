class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks()

mark.age = 10

print(mark.age)


class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("C.getter")
        return self._x

    @x.setter
    def x(self, value):
        print("C.setter")
        self._x = value

    @x.deleter
    def x(self):
        print("C.deleter")
        del self._x


cc = C()
cc.x = 1
print(cc.x)
