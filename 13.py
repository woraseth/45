from math import *

def mul(a, b):
  m = []
  for r in range(len(a)):
    t = []
    for c in range(len(b[0])):
      t.append(sum(a[r][i] * b[i][c] for i in range(len(a[0]))))
    m.append(t)
  return m

x, y = (int(s) for s in input().split())
th = radians(int(input()))
fx, fy = (int(s) for s in input().split())

m  = [[x],[y],[1]]
t0 = [[1,0,-fx],[0,1,-fy],[0,0,1]]
r  = [[cos(th),-sin(th),0],[sin(th),cos(th),0],[0,0,1]]
t1 = [[1,0,fx], [0,1,fy], [0,0,1]]

r = mul(t1,mul(r,mul(t0,m)))
print('%.3f %.3f' % (r[0][0], r[1][0]))
'''
a = [[1,2,3],[4,5,6]]
b = [[7,8],[9,10],[11,12],]
mul(a,b)  # [[58, 64], [139, 154]]

a = [[3, 4, 2]]
b = [[13,9,7,15],[8,7,4,6],[6,4,0,3],]
mul(a,b)  # [[83, 63, 37, 75]]
'''
