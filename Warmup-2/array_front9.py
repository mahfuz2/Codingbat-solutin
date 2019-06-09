def array_front9(nums):
  ar = False
  if len(nums)<=4:
    for i in range(len(nums)):
      if nums[i]==9:
        ar = True
        break
    return ar
  else:
    for i in range(4):
      if nums[i]==9:
        ar = True
        break
    return ar

print(array_front9([1, 2, 9, 3, 4]),
array_front9([1, 2, 3, 4, 9]),
array_front9([1, 2, 3, 4, 5]))