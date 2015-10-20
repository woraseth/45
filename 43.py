# 60 - social network

jace = input().split()
lala = input().split()
a = [j for j in jace if j in lala]
a.append('Lalana')
a.sort()
print(', '.join(a))
