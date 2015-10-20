# moore machine
binstr = input()
state = int(input())
d = {}
out = {}
cur = None
for _ in range(state):
  a = input().split()
  d[a[0]] = (a[1], a[2])
  out[a[0]] = a[2]
  if cur == None:
    cur = a[0]

s = ''
for b in binstr:
  b = int(b)
  cur = d[cur][b]
  s += cur
print(s)
