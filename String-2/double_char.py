def double_char(str):
  new = ""
  for i in range(len(str)):
    new = new+str[i]+str[i]
  return new

print(double_char('The'),
double_char('AAbb'),
double_char('Hi-There'))