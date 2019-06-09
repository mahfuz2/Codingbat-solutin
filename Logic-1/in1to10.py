def in1to10(n, outside_mode):
  if outside_mode:
    if n<=1 or n>=10:
      return True
    else:
      return False
  else:
    if 1<=n<=10:
      return True
    else:
      return False

print(in1to10(5, False),
in1to10(11, False),
in1to10(11, True))