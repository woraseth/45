# 29 - my son was born on Loy Kratong day

amas = [34,36,39,42,45,47,50,53,55]
awan = [40,43,49,52]
norm_day, awan_day, amas_day = 354, 355, 384
days = 0
for year in range(55, 33, -1):
  from datetime import date, timedelta
  print(date(2012,12,14) - timedelta(days=days+16))
  if year in amas:
    days += amas_day
  elif year in awan:
    days += awan_day
  else:
    days += norm_day
