a = ['ab', 'aB', 'Ab', 'AB', ]
a.sort()
#a = ['ABC', 'ABc', 'AbC', 'Abc', 'aBC', 'aBc', 'abC', 'abc']
d = {}
for i in range(len(a)):
  for j in range(len(a)):
    s = a[i][0] + a[j][0] + a[i][1] + a[j][1]# + a[i][2] + a[j][2]
    caps = len(list(filter(lambda c : c == c.upper(), s)))
    print('%s (%d), ' % (s, caps), end='')
