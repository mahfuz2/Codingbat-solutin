def left2(str):
  if len(str)<=2:
    return str
  else:
    return str[2:]+str[:2]

print(left2('Hello'),
left2('java'),
left2('Hi'))