tt = int(input())
for _ in range(tt):
  a, b = (int(s) for s in input().split())
  a, b = max(a, b), min(a, b)
  c = 0
  cnt = 0
  while a != 0:
    c = 1 if (c + (a%10) + (b%10)) > 9 else 0
    cnt += c
    a //= 10
    b //= 10
  print(cnt)
