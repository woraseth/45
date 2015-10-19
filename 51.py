# lat long
def f(a, d):
  a[0] = int(d)
  d -= int(d)
  d *= 60
  a[1] = int(d)
  d -= int(d)
  d *= 60
  a[2] = int(round(d))
  #a[2] = int(d)

tt = int(input())
for _ in range(tt):  
  lat, lng = (float(s) for s in input().split())
  if lat < 0: 
    dir_lat = 'S'
    lat *= -1
  else:
    dir_lat = 'N'
  if lng < 0: 
    dir_lng = 'W'
    lng *= -1
  else:
    dir_lng = 'E'
  lats = [0] * 3
  lngs = [0] * 3
  f(lats, lat)
  f(lngs, lng)
  print('%02d%02d%02d%s' % (*lats, dir_lat), end=' ')
  print('%02d%02d%02d%s' % (*lngs, dir_lng))
