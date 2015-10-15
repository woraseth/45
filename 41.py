def f(n):
  if ord(n[0]) > ord(n[1]):
    return n[1] + n[0]
  else:
    return n
    
grp_gene = {'A' :['AA', 'AO'],
         'B' :['BB', 'BO'],
         'AB':['AB'],
         'O' :['OO']}
gene_grp = {'AA': 'A',  'AO': 'A',
            'BB': 'B',  'BO': 'B',
            'AB': 'AB', 'OO': 'O'}
tt = int(input())
for _ in range(tt):
  parents = input().split()
  dad = grp_gene[parents[0]]
  mom = grp_gene[parents[1]]
  s = set()
  for d in dad:
    for m in mom:
      s.add(f(d[0] + m[1]))
      s.add(f(d[0] + m[0]))
      s.add(f(m[0] + d[1]))
      s.add(f(d[1] + m[1]))
  s = set(gene_grp[i] for i in s)
  print(' '.join(sorted(s)))
