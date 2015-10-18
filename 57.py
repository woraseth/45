def next(a, i):
  i = (i + 1) % len(a)
  while a[i]:
    i = (i + 1) % len(a)
  return i

def search(n): 
  for step in range(2,1000):
    a = [False] * n
    index = 0
    count = 0
    while True:
      for _ in range(step):
        index = next(a, index)
      if index == 0:
        if count == n - 1:
          return step
        else:
          break
      a[index] = True
      count += 1
      
tt = int(input())
for _ in range(tt):
  print(search(int(input())))
