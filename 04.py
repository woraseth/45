# 04 - pris

from math import gcd  # python 3.5

tt = int(input())
for _ in range(tt):
  c, d = (int(s) for s in input().split('/'))
  g = gcd(c, d)
  c //= g
  d //= g
  n = c // d
  if n == 0 and c % d == 0:
    print(0)
  elif n != 0 and c % d != 0:
    print('%d %d/%d' % (n, c % d, d))
  elif n != 0 and c % d == 0:
    print(n)
  else:
    print('%d/%d' % (c % d, d))
