def prime(n):
  is_prime = [True] * n
  is_prime[0] = False
  is_prime[1] = False
  for i in range(2, n):
    if is_prime[i]:
      for j in range(i+i, n, i):
        is_prime[j] = False
  return is_prime
  	
print(prime(20))
