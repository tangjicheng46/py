# while True:
#     try:
#         x = int(input("pls in:"))
#         break
#     except:
#         print("Oops, invalid.")

# class B(Exception):
#     pass


# class C(B):
#     pass


# class D(C):
#     pass


# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

try:
    raise Exception("Hello", "World")
except Exception as inst:
    print(inst)
    print(type(inst))
    print(inst.args)
    print(type(inst.args))
