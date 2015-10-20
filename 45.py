# mind graffiti

def dec(c):
  cc = ord(c)
  if ord('a') <= cc and cc <= ord('z'):
    cc += 3
    if cc > ord('z'):
      cc = cc - ord('z') + ord('a') - 1
  elif ord('A') <= cc and cc <= ord('Z'):
    cc += 3
    if cc > ord('Z'):
      cc = cc - ord('Z') + ord('A') - 1
  return chr(cc)
  
cipher = input()
plain = ''
for c in cipher:
  plain += dec(c)
print(plain)
