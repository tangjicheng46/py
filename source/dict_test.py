# python 字典dict的用法

d1 = dict()
d1['one'] = 1
d1['two'] = 2
d1['three'] = 3

d2 = {'one': 1, 'two': 2, 'three': 3}

print(d1 == d2)

for i in d1.items():
    print(i, type(i), i[1])

print(d1.keys(), type(d1.keys()))
temp = d1.values()
print(temp, type(d1.values()))

d1['one'] = -1
for i in d1.items():
    print(i[0], " -> ", i[1])

print(temp)

print(dict([(v, k) for (k, v) in d1.items()]))
