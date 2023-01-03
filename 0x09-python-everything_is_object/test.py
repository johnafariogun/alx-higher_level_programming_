#!/usr/bin/python3
def assign_value(n, v):
    n = v
a=()
b=(1,3)
c=(1, )
d =()
e = ()
print('is',d is e)
print(type(a))
print(type(b))
print(type(c))
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(id(l1))
l1 =l1 + [4]
print(id(l1))
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
