# 41 - polygene

n = int(input())
a = [1, 1]
for i in range(n-1):
  a = [1 if (j == 0 or j == len(a)) else a[j-1]+a[j] for j in range(len(a) + 1)]
print(':'.join(str(i) for i in a))
