
def front_back(str):
  if len(str)<=1:
    return str
  else:
    mid = str[1:len(str)-1]
    return (str[len(str)-1]+mid+str[0])

print(front_back('code'),
front_back('a'),
front_back('ab'))