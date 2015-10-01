# angle between two vector

a = [-2, -1]
b = [2, -1]

from math import *
x = sum(a[i] * b[i] for i in range(len(a)))
x /= sqrt(sum(a[i] * a[i] for i in range(len(a))))
x /= sqrt(sum(b[i] * b[i] for i in range(len(a))))
angle = acos(x)
print(degrees(angle))
