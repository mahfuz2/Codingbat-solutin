
def make_out_word(out, word):
  return out[:2]+word+out[2:]

print(make_out_word('<<>>', 'Yay'),
make_out_word('<<>>', 'WooHoo'),
make_out_word('[[]]', 'word'))