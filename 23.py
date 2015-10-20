# fill color

def fill(x, y):
  m[y][x] = 1
  if m[y][x-1] == 0: fill(x-1,y)
  if m[y][x+1] == 0: fill(x+1,y)
  if m[y-1][x] == 0: fill(x,y-1)
  if m[y+1][x] == 0: fill(x,y+1)

width, height = (int(s) for s in input().split())
m = []
for _ in range(height):
  m.append([int(s) for s in input()])
x, y = (int(s) for s in input().split())
fill(x-1, y-1)
for i in range(height):
  print(''.join(str(n) for n in m[i]))
