def shorten(s):
  if len(s) <= 10:
    return s + ' ' * (10 - len(s))
  else:
    return s[:7] + '...'
    

d = {}
while True:
  line = input().split()
  if line[0] == 'end':
    break
  price = int(line[len(line)-1])
  prod = " ".join(line[:len(line)-1])
  d[prod] = (1, price) if prod not in d else (d[prod][0] + 1, price)
a = [p for p in d]
a.sort()
sm = 0
for p in a:
  price = d[p][0] * d[p][1]
  sm += price
  print('%s %2d %5d' % (shorten(p), d[p][0], price))
print('%19d' % sm)
