# 08 - pris

from math import gcd  # python 3.5

tt = int(input())
for _ in range(tt):
  c, d = (int(s) for s in input().split('/'))
  g = gcd(c, d)
  c //= g
  d //= g
  if c // d != 0:
    print(c // d, end=' ')
  if c % d != 0:
    print('%d/%d' % (c % d, d))
