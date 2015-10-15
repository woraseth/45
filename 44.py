# 44 - alumirite

def read_int(s, start):
  i = start
  while i < len(s) and '0' <= s[i] and s[i] <= '9':
    i += 1
  return 1 if i == start else int(s[start:i]), i
  
def add(d, s):
  mul, i = read_int(s, 0)
  while i < len(s):
    element = s[i]
    i += 1
    sub, i = read_int(s, i)
    d[element] = d[element] + sub * mul if element in d else sub * mul
    
def process(s):
  d = {}
  for t in s.split('+'):
    add(d, t)
  return d
  
tt = int(input())
for _ in range(tt):
  left, right = input().split('=')
  left = process(left)
  right = process(right)
  print('balance' if left == right else 'imbalance')
