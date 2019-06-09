
def makes10(a, b):
  if a==10 or b==10:
    return True
  elif a+b==10:
    return True
  else:
    return False

print(makes10(9, 10),
makes10(9, 9),
makes10(1, 9))