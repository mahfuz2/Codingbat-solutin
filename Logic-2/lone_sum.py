def lone_sum(a, b, c):
  if a!=b and b!=c and a!=c:
    return a+b+c
  elif (a==b or b==a) and a!=c:
    return c
  elif (b==c or c==b) and a!=b:
    return a
  elif (a==c or c==a) and a!=b:
    return b
  elif a==b and b==c:
    return 0

print(lone_sum(1, 2, 3),
lone_sum(3, 2, 3),
lone_sum(3, 3, 3))