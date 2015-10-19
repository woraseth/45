# coin
# c_3 + 1 < x < c_m + c_m-1

def f(n):
  m = n
  coin = [10,5,2,1]
  count = [0] * 4
  index = 0
  while n > 0:
    if n >= coin[index]:
      n -= coin[index]
      count[index] += 1
    else:
      index += 1
  s = []
  for t in zip(coin, count):
    if t[1] != 0:
      s.append('%dx%d' % t)
  print('%d=%s' % (m, '+'.join(s)))

tt = int(input())
for _ in range(tt):
  f(int(input()))
