# 06 - grade

tt = int(input())
grade = {'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2, 'D+':1.5, 'D':1, 'F':0}
sum_c = 0
sum_w = 0
for _ in range(tt):
  a = input().split()
  c = int(a[0])
  g = grade[a[1]]
  sum_c += c
  sum_w += c * g
print('%.2f' % (sum_w / sum_c))
  
