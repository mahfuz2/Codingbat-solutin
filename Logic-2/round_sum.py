def round_sum(a, b, c):
  def round_sums(x):
    if x<5:
      return 0
    elif 4<x<15:
      return 10
    elif 14<x<25:
      return 20
    elif 24<x<35:
      return 30
    elif 34<x<45:
      return 40
    elif 44<x<55:
      return 50
    else:
      return 0
  d=round_sums(a)
  e=round_sums(b)
  f=round_sums(c)
  return d+e+f

print(round_sum(16, 17, 18),
round_sum(12, 13, 14),
round_sum(6, 4, 4) )