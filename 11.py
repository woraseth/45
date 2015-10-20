# numberg light pole

def prime(n):
  is_prime = [True] * n
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n):
    if is_prime[i]:
      for j in range(i+i, n, i):
        is_prime[j] = False
  return is_prime
  	
is_prime = prime(1000000)
tt = int(input())
for _ in range(tt):
  n = int(input())
  i = 0
  while n != 0:
    i += 1
    if is_prime[i]:
      n -= 1
  print(i)
