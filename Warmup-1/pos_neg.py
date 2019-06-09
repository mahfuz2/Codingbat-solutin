
def pos_neg(a, b, negative):
  if ((a<0 and b<0) and negative):
    return True
  elif  ((a<0 and b>0) or (a>0 and b<0))  and not negative:
    return True
  else:
    return False

print(pos_neg(1, -1, False),
pos_neg(-1, 1, False),
pos_neg(-4, -5, True))