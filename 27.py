# Fairarie, the Naughty Fairy

def next(time):
  if time[1] == 59:
    time[1] = 0
    time[0] += 1
    if time[0] == 24:
      time[0] = 0
  else:
    time[1] += 1

tt = int(input())
for _ in range(tt):
  time = [int(s) for s in input().split(':')]
  count = 0
  while time != [5, 59]:
    next(time)
    count += 1
  print(count)
