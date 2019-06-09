
def close_far(a, b, c):
	if abs(a-b) <2:
		if abs(a-c) >= 2 and abs(b-c) >= 2:
			return True
	if abs(a-c) <2:
		if abs(a-b) >= 2 and abs(b-c) >= 2:
			return True
	return False


print(close_far(1, 2, 10),
close_far(1, 2, 3),
close_far(4, 1, 3) )