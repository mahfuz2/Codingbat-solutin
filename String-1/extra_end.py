
def extra_end(str):
  if len(str)<=2:
    return str*3
  else:
    return str[len(str)-2:]*3

print(extra_end('Hello'),
extra_end('ab'),
extra_end('Hi'))