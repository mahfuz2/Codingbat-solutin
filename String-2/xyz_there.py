def xyz_there(str):
	#if str[:3] == 'xyz':
		#return True
	if str.startswith('xyz'):
		return True

	for i in range(1, len(str)):
		if str[i-1] != '.' and str[i:i+3] == 'xyz':
			return True

	return False

print(xyz_there('abcxyz'),
xyz_there('abc.xyz'),
xyz_there('xyz.abc'))