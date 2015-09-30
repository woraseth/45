tt = int(input())
for _ in range(tt):
  f = int(input())
  n = 0
  while True:
    x0 = 1;
    for i in range(n+1):
      x0 += i
    if x0 >= f:
      break
    n += 1
  print(n)
