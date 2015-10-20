import subprocess
import os.path

N = 45
h = [0] * N
for i in range(1, N + 1):
  try:
    print(i)
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
      h[i-1] = sm
  except:
    print('error at %d' % i)

with open('solution.45.txt', 'w') as f:
  for i in range(N):
    print('%02d %d' % (i+1, h[i]), file=f)
