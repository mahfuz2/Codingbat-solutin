def make_bricks(small, big, goal):
  if goal>=big*5:
    remain = goal - (big*5)
  else:
    remain = goal%5
  if small>=remain:
    return True
  else:
    return False

print(make_bricks(3, 1, 8),
make_bricks(3, 1, 9),
make_bricks(3, 2, 10))