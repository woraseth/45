# 08 - pris

from math import gcd  # python 3.5

a, b = (int(s) for s in input().split('/'))
tt = int(input())
for _ in range(tt):
  c, d = (int(s) for s in input().split('/'))
  g = gcd(c, d)
  d /= g
  if d == b and a == c/g:
    print('1', end='')
  else:
    print('0', end='')
