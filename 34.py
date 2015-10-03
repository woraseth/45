# 34 - allergic to bangkok

tt = int(input())
m = [[' '] * 70 for i in range(70)]
for _ in range(tt):
  xx, ww, hh = (int(s) for s in input().split())
  xx -= 1
  for h in range(hh):
    for w in range(ww):
      m[h][xx+w] = 'X'
for h in reversed(range(70)):
  if 'X' in m[h]:
    print(''.join(m[h]))
