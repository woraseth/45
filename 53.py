# tourbillon

tt = int(input())
for _ in range(tt):
  line = input()
  a = line.split(':')
  hour = int(a[0])
  if hour == 12:
    hour = 0
  minute = int(a[1])
  minRatio = minute / 60;
  hourDegree = (hour + minRatio) * 30;
  minDegree = minute * 6;
  diff = abs(hourDegree - minDegree);
  if diff > 180:
    diff = 360 - diff
  print('%.3f' % diff)
