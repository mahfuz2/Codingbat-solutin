
def first_two(str):
  if len(str)<=2:
    return str
  else:
    return str[:2]

print(first_two('Hello'),
first_two('abcdefg'),
first_two('ab'))