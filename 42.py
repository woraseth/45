#a = ['ab', 'aB', 'Ab', 'AB', ]
a = ['ABC', 'ABc', 'AbC', 'Abc', 'aBC', 'aBc', 'abC', 'abc']
d = {}
for i in range(len(a)):
  for j in range(len(a)):
    s = a[i][0] + a[j][0] + a[i][1] + a[j][1] + a[i][2] + a[j][2]
    caps = len(list(filter(lambda c : c == c.upper(), s)))
    if caps in d:
      d[caps].append(s)
    else:
      d[caps] = [s]
for k in d:
  d[k].sort()
n = [k for k in d]
n.sort()
n.reverse()
for i in n:
  print('%d (%s)' % (len(d[i]), ', '.join(d[i])))
