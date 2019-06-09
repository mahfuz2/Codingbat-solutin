def squirrel_play(temp, is_summer):
  if not(is_summer):
    if 60<=temp<=90:
      return True
    else:
      return False
  else:
    if 60<=temp<=100:
      return True
    else:
      return False

print(squirrel_play(70, False),
squirrel_play(95, False),
squirrel_play(95, True))