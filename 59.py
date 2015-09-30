# 59 - it was called 'Directory'

freq = {}
while True:
  try:
    s = input()
    s = s[:s.rfind('\\')]
    if s in freq:
      freq[s] += 1
    else:
      freq[s] = 1
  except:
    break

a = list(freq)
a.sort()
for s in a:
  print(s, freq[s])
