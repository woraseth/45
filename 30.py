a = [int(s) for s in input().split()]
mean = sum(a) / len(a)
d = [(a[i] - mean) ** 2 for i in range(len(a))]
var = sum(d) / len(d)
from math import sqrt
print('%.3f' % sqrt(var))
