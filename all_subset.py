total_bit = 5
for i in range(2**total_bit):
  for j in range(total_bit):
    if (i & (1 << (total_bit-j-1))) == 0:
      print(0, end='')
    else:
      print(1, end='')
  print()
