# not so cool
def prime(n):
  is_prime = [False, False]
  is_prime.extend([True] * n)
  for i in range(2, n):
    if is_prime[i]:
      for j in range(i+i, n, i):
        is_prime[j] = False
  return [i for i in range(n) if is_prime[i]]

def factor(n):
  f = []
  i = 0
  while n != 1:
    while n % p[i] == 0:
      n //= p[i]
      f.append(p[i])
    i += 1
  return f if len(f) > 0 else [1]
    
p = prime(1000)
for _ in range(int(input())):
  f = factor(int(input()))
  s = []
  while len(f) != 0:
    t = '*'.join(str(i) for i in factor(f.count(f[0])))
    s.append('%d**(%s)' % (f[0], t))
    f = [i for i in f if i != f[0]]
  print('*'.join(s))
