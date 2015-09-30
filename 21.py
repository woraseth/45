# 21 - spell cheque

tt = int(input())
for _ in range(tt):
  vocabs = set(input().split())
  words = input().split(' ')
  print(' '.join(map(lambda s : s if s in vocabs else s.upper(), words)))
