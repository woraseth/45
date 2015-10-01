# 37 - gag game

from random import shuffle

tt = int(input())
for _ in range(tt):
  deck = [int(s) for s in input().split()]
  run = 1000000
  count = 0
  for i in range(run):
    shuffle(deck)
    b = [0] * 5
    for i in range(5):
      b[i] = deck[i]
    b.sort()
    if b[0] < b[1] and b[1] < b[2] and b[2] < b[3] and b[3] < b[4]:
      count += 1
  print('%.3f' % (count*100/run))
