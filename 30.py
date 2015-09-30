# 30 - as love is

tt = int(input())
for t in range(tt):
  if t != 0: print()
  n = int(input())
  if n == 0: break
  a = [
    ' CC CC',
    'CCCCCCC',
    ' CCCCC',
    '  CCC',
    '   C',]
  for i in range(len(a)):
    s = a[i]
    for j in range(n):
      for k in range(len(s)):
        c = s[k]
        for l in range(n):
          print(c, end='')
      print()
