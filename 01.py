# 01 - shopaholic

tt = int(input())
for t in range(tt):
  a = [int(s) for s in input().split()]
  a.sort()
  a.reverse()
  if len(a) < 3:
    total = sum(a)
  else:
    total = sum(a) - a[2]
  print('%d: %d Baht' % (t+1, total))
