# 09 - good brother

tt = int(input())
for _ in range(tt):
  mx = -1
  quota = int(input())
  a = [int(s) for s in input().split()]
  total_bit = len(a)
  for i in range(2**total_bit):
    sm = 0
    for j in range(total_bit):
      if (i & (1 << (total_bit-j-1))) != 0:
        sm += a[j]
    if mx < sm and sm <= quota:
      mx = sm
  print(quota-mx)
