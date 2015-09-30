# 39 - intania 

p = ['', 'k', 'M', 'G', 'T', 'P', 'E']
def engineer(s):
  exp = len(s) - 1
  exp //= 3
  pos = len(s) - exp * 3
  s = s[:pos] + '.' + s[pos:]
  s = s.rstrip('0').rstrip('.')
  return s + '%s' % (p[exp])

tt = int(input())
for _ in range(tt):
  print(engineer(input()))
