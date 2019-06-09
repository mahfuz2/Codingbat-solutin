def no_teen_sum(a, b, c):
  def fix_teen(n):
    if 13<=n<15 or 17<=n<20:
      return 0
    else:
      return n
  f = fix_teen(a)
  d = fix_teen(b)
  e = fix_teen(c)
  return f+d+e

print(no_teen_sum(1, 2, 3),
no_teen_sum(2, 13, 1),
no_teen_sum(2, 1, 14) )