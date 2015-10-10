# 08 - quarter

target = int(float(input())*100)
cnt = 0
for a in range(1 + target // 100):
  for b in range(1 + target // 50):
    for c in range(1 + target // 25):
      if a*100 + b*50 + c*25 == target:
        # print(a,b,c)
        cnt += 1
print(cnt)
