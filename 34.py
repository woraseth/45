# 34 - allergic to bangkok

tt = int(input())
m = [[' '] * 70 for i in range(70)]
for _ in range(tt):
  x, width, height = (int(s) for s in input().split())
  x -= 1
  for h in range(height):
    for w in range(width):
      m[h][x+w] = 'X'
for h in reversed(range(70)):
  if 'X' in m[h]:
    print(''.join(m[h]))
