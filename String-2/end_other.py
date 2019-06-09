def end_other(a, b):
  c = a.lower()
  d = b.lower()
  for i in range(max(len(a),len(b))):
    if c==d[len(d)-len(c):] or d==c[len(c)-len(d):]:
      return True
    else:
      return False

print(end_other('Hiabc', 'abc'),
end_other('AbC', 'HiaBc'),
end_other('abc', 'abXabc'))