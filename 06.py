# 06 - grade

cr = [int(s) for s in input().split()]
tt = int(input())
grade = {'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2, 'D+':1.5, 'D':1, 'F':0}
for _ in range(tt):
  sum_c = 0
  sum_w = 0
  for i in enumerate(input().split()):
    c = cr[i[0]]
    g = grade[i[1]]
    sum_c += c
    sum_w += c * g
  print('%.2f' % (sum_w / sum_c))
