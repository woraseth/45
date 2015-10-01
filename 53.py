# 53 - world order

from math import *

def distance(p1, p2):
  return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

tt = int(input())
for _ in range(tt):
  a = [[float(s) for s in input().split()] for i in range(3)]
  d = [distance(a[i], a[i-1]) for i in range(3)]
  if all(abs(d[i]-d[i-1]) < 1e-4 for i in range(3)):
    print('Equilateral')
  elif any(abs(d[i]-d[i-1]) < 1e-4 for i in range(3)):
    print('Isosceles')
  else:
    print('Scalene')
