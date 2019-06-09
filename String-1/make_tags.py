
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

print(make_tags('i', 'Yay'),
make_tags('i', 'Hello'),
make_tags('cite', 'Yay'))