# 02 - backspace

a = [0,2,4,6,8,1,3,5,7,9]
tt = int(input())
for _ in range(tt):
  s = input()
  sm = 0
  for i in range(len(s)):
    c = ord(s[i]) - 48
    if i % 2 == 0:
      sm += a[c]
    else:
      sm += c
  print((sm*9)%10) 
