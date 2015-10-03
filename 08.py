# 08 - pris

from math import gcd  # python 3.5

tt = int(input())
for _ in range(tt):
  c, d = (int(s) for s in input().split('/'))
  g = gcd(c, d)
  print('%d/%d' % (c / g, d / g))
