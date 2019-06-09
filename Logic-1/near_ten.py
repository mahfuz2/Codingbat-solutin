def near_ten(num):
  a=num%10
  if a<=2 or (10-a)<=2:
    return True
  else:
    return False

print(near_ten(12),
near_ten(17),
near_ten(19))