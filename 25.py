# gag game

from random import shuffle

tt = int(input())
for _ in range(tt):
  deck = [int(s) for s in input().split()]
  run = 1000000
  count = 0
  for i in range(run):
    shuffle(deck)
    b = deck[:5]
    b.sort()
    if b[0] + 1 == b[1] and b[1] + 1 == b[2] and b[2] + 1 == b[3] and b[3] + 1 == b[4]:
      count += 1
  print('%.0f' % (count*100/run))
