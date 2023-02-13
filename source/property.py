class A:
    def __init__(self, birth=0, age=0):
        self._birth = birth
        self._age = age

    @property
    def birth(self):
        print("Birth is : ", self._birth)
        return self._birth

    @property
    def age(self):
        print("Age is ", self._age)
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        print("Age is setted to ", self._age)


if __name__ == "__main__":
    a1 = A(1999, 20)
    # a1.birth = 1988
    a1.age = 31
