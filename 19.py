# 19 - Man, the fortuneteller

nicknames = input().split()
d = {}
for n in nicknames:
  s = n[1:].upper()
  if s in d:
    d[s].append(n)
  else:
    d[s] = [n]
for key in d:
  d[key].sort()
tt = int(input())
for _ in range(tt):
  names = input().split()
  print(' '.join(d[names[0][0] + names[1][0]]))
