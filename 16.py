# Man, the fortuneteller

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
  fn, ln = input().split()
  if fn[0] + ln[0] in d:
    print(' '.join(d[fn[0] + ln[0]]))
  else:
    print('You should change your firstname or lastname')
