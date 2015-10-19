# Tetranacci

def f(n):
  a = [0,1,1,2]
  if n > 3:
    a.extend([0] * (n-3))
  for i in range(4, len(a)):
    a[i] = a[i-1]+a[i-2]+a[i-3]+a[i-4] 
  return a[n]

tt = int(input())
for _ in range(tt):
  print(f(int(input())))
