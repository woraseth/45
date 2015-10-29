# Jelly Wall

def trapezoidal(f, a, b, n):
  h = (b - a) / n
  s = sum(f(a + i*h) for i in range(1, n))
  return (f(a) + 2*s + f(b)) * h / 2

tt = int(input())
for _ in range(tt):
  n = int(input())
  print('%.1f' % (30 * trapezoidal(lambda x : -3*x*x + 12, -2, 2, n))) 
