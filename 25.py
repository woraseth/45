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
    if all(b[i] + 1 == b[i + 1] for i in range(4)):
      count += 1
  print('%.0f' % (count*100/run))
