def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars>=40:
      return True
    else:
      return False
  else:
    if cigars>=40 and cigars<=60:
      return True
    else:
      return False

print(cigar_party(30, False),
cigar_party(50, False),
cigar_party(70, True))