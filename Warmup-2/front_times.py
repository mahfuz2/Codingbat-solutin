

def front_times(str, n):
  if len(str)<=3:
    return str*n
  else:
    return str[:3]*n

print(front_times('Chocolate', 2),
front_times('Chocolate', 3),
front_times('Abc', 3))