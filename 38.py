tt = int(input())
for _ in range(tt):
  a = [int(s) for s in input().split()]
  while len(a) != 4:
    a = [a[i-1] if a[i-1] < a[i] else a[i] for i in range(1,len(a), 2)]
  a.sort()
  print(a[0], a[2], a[1])
