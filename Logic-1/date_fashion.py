def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  else:
    if you>=8 or date>=8:
      return 2
    else:
      return 1

print(date_fashion(5, 10),
date_fashion(5, 2),
date_fashion(5, 5))