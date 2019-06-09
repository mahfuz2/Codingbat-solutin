def front3(str):
  if len(str)<3:
    return str+str+str
  else:
    return str[:3]+str[:3]+str[:3]

print(front3('Java'),
front3('Chocolate'),
front3('abc'))