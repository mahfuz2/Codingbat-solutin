def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed<=65:
      return 0
    elif 65<speed<=85:
      return 1
    else:
      return 2
  else:
    if speed<=60:
      return 0
    elif 60<speed<=80:
      return 1
    else:
      return 2

print(caught_speeding(60, False),
caught_speeding(65, False),
caught_speeding(65, True))