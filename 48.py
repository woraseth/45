# cry so hard

tt = int(input())
for _ in range(tt):
  line = input()
  found = False
  for i in range(len(line)-4):
    for j in range(i+4, len(line)-3):
      if line[i:i+4] == line[j:j+4]:
        found = True
        print(line[i:i+4])
        break
    else:
      continue
    break

  if not found:
    print('Not found')
