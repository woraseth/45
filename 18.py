def alphanum(c):
  c = ord(c)
  return (ord('a') <= c and c <= ord('z')) or \
         (ord('0') <= c and c <= ord('9'))
  
words = input().split()
tt = int(input())
for _ in range(tt):
  password = input()
  lower = password.lower()
  if len(password) < 10 or \
     password == password.upper() or \
     password == lower or \
     any(w in lower for w in words) or \
     all(alphanum(c) for c in lower):
    print('weak password')
  else:
    print('strong password')
