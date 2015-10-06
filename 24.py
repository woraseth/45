# 24 - PS

template = input()
template = template.replace('<', '{')
template = template.replace('>', '}')

tt = int(input())
for _ in range(tt):
  a = [s.strip() for s in input().split(',')]
  a.insert(0, None)
  print(template.format(*a))
