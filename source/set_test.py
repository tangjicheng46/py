# python set的用法

s1 = {1, 3, 5}
s2 = set((2, 4, 6))
s3 = {1, 2, 3, '4'}

print("union: ", s1.union(s2))
print("diff: ", s1.difference(s2))
print("intersection: ", s1.intersection(s3))

print("for loop s3: ")
s3.update(s2)
s3.add(10)
s3.remove(1)
s3.discard(100)
for i in s3:
    print(i)

print(10 in s3)
