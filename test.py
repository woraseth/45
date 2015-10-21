import subprocess
import sys
import os.path

def read_solve():
  if os.path.isfile('solved.45.txt'):
    with open('solved.45.txt', 'r') as f:
      return f.read().split()
  else:
    return []
    
def write_solve(a):
  with open('solved.45.txt', 'w') as f:
    f.write(a)
    
i = int(sys.argv[1])
if os.path.isfile('%02d.in2' % i):
  in_file = open('%02d.in2' % i, 'r')
  out_file = open('%02d.out2' % i, 'w')
  subprocess.call(["python", "%02d.py" % i], stdin=in_file, stdout=out_file)
  in_file.close()
  out_file.close()
else:
  out_file = open('%02d.out2' % i, 'w')
  subprocess.call(["python", "%02d.py" % i], stdout=out_file)
  out_file.close()
  
with open('%02d.out2' % i, 'r') as f:
  sm = 0
  index = 1
  for line in f:
    for c in line:
      c = ord(c)
      if 32 <= c and c <= 126:
        sm += c * index
        index += 1
        if index > 9991:
          index = 1
        sm %= 99991
  h = sm
  
with open('solution.45.txt', 'w') as f:
  for line in f:
    a = [int(s) for s in line.split()]
    if a[0] == i:
      solved = read_solve()
      if h == a[1]:
        # correct
        if str(i) not in solved:
          solved.append(str(i))
        write_solve(solved) 
        print('Correct. You have % problems remaining.' % (45 - len(solved)))
      else:
        print('Incorrect. You have % problems remaining.' % (45 - len(solved)))
      break
