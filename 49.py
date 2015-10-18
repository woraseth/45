#  music (note, octave) to freq

a = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
d = dict(zip(a, range(len(a))))

tt = int(input())
for _ in range(tt):
  line = input().split(' ')
  note = line[0]
  octave = int(line[1])
  step = d[note] - d['A']
  n = (octave - 4) * 12 + step
  print('%s%d %.3f' % (note, octave, 440 * 2**(n/12)))
