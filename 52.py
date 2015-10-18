#  pie chart

tt = int(input())
for _ in range(tt):
  a = [int(s) for s in input().split()]
  sm = sum(a)
  deg = 0;
  for i in range(len(a)-1):
    deg += a[0] * 360 / sm
    print('%.2f' % deg, end=' ')
  print()
