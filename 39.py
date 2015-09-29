# intania 

def engineer(s):
  exp = len(s) - 1
  exp //= 3
  pos = len(s) - exp * 3
  s = s[:pos] + '.' + s[pos:]
  s = s.rstrip('0').rstrip('.')
  return s + 'e%d' % (exp * 3)

tt = int(input())
for _ in range(tt):
  print(engineer(input()))
