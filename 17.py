# how do we end up at this point?

s = input()
sum = 0
for c in s:
  c = ord(c)
  if 0x30 <= c and c <= 0x39:
    sum += 1
  else:
    if c < 10:
      sum += 1
    elif c < 100:
      sum += 2
    else:
      sum += 3
print(sum)
