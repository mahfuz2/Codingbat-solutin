def make_chocolate(small, big, goal):
  n = (big*5)
  if goal>=n:
    remain = goal-n
  else:
    remain = goal%5
  if remain <= small:
    return remain
  else:
    return -1

print(make_chocolate(4, 1, 9),
make_chocolate(4, 1, 10),
make_chocolate(4, 1, 7))