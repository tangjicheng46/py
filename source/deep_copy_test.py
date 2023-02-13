import copy

a = [1, 2, 3, [4, 5, 6]]
b = a
c = a.copy()
d = copy.deepcopy(a)

a[0] = -1
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)

a[3][0] = -1
print("-----")
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
