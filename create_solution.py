import subprocess

N = 60
h = [0] * N
for i in range(1, N + 1):
  try:
    in_file = open('%02d.in2' % i, 'r')
    out_file = open('%02d.out2' % i, 'w')
    subprocess.call(["python", "%02d.py" % i], stdin=in_file, stdout=out_file)
    in_file.close()
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

with open('solution.txt', 'w') as f:
  for i in range(N):
    print('%02d %d' % (i, h[i]), file=f)
