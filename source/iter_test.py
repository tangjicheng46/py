class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# TODO
a = Reverse('1234')
# a = [1, 2, 3, 4]
for i in a:
    print('i', i)
    for j in a:
        print('j', j)

for j in a:
    print('k', j)
