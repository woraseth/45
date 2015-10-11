# 10 - license plate
tt = int(input())
for _ in range(tt):
  s = input()
  d0 = 10**(s.index('(') - s.index('.') - 1)
  d1 = d0 * 10**(s.index(')') - s.index('(') - 1) - d0
  s1 = s[s.index('(')+1:s.index(')')]
  s0 = s[:s.index('(')].replace('.', '')
  #print(d0, d1, s0, s1)
  n = int(s0+s1) - int(s0)
  from math import gcd
  g = gcd(n, d1)
  print(''.join((str(n // g), '/', str(d1 // g))))
