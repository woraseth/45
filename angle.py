# angle between two vectors

a = [-2, -1]
#b = [2, -1]
b = [0, 2]
from math import *
x = sum(a[i] * b[i] for i in range(len(a)))
x /= sqrt(sum(i*i for i in a))
x /= sqrt(sum(i*i for i in b))
angle = acos(x)
print(degrees(angle))
