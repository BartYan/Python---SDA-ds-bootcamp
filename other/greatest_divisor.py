def greatDivi(a, b):

    aList = []
    bList = []

    for i in range(a):
        aList += [int(a / (i + 1))]

    for i in range(b):
        bList += [int(b / (i + 1))]

    check = list(set(aList).intersection(bList))
    res = max(check)
    print(res)

print(greatDivi(30, 50))



# 2
# def NWD(x,y):
#     if x >= y:
#         if x%y == 0:
#             return y
#         else:
#             z = x%y
#             return NWD(x,z)
#     else:
#         if y%x == 0:
#             return x
#         else:
#             z = y%x
#             return NWD(y,z)
#
# print(NWD(3,40))

# 3
# def nwd(a, b):
#     while b:
#         temp = a
#         a = b
#         b = temp%b
#     return a

#4
# def nwd(a, b):
#     if b > 0:
#         return nwd(b, a%b)
#     return a