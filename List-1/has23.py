def has23(nums):
  if nums[0]==2 or nums[1]==2:
    return True
  elif nums[0]==3 or nums[1]==3:
    return True
  else:
    return False

print(has23([2, 5]),
has23([4, 3]),
has23([4, 5]) )