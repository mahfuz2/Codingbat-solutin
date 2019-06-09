def cat_dog(str):
  count1 = 0
  count2 = 0
  for i in range(len(str)):
    if str[i:i+3] == "cat":
      count1 = count1+1
    if str[i:i+3]== "dog":
      count2=count2+1
  if count1==count2:
    return True
  else:
    return False


print(cat_dog('catdog'),
cat_dog('catcat'),
cat_dog('1cat1cadodog'))