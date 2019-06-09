
def without_end(str):
  if len(str)<=2:
    return ""
  else:
    return str[1:len(str)-1]

print(without_end('Hello'),
without_end('java'),
without_end('coding'))