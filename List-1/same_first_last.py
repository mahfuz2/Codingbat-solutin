def same_first_last(nums):
  if len(nums)>=1 and (nums[0]==nums[-1]):
    return True
  else:
    return False

print(same_first_last([1, 2, 3]),
same_first_last([1, 2, 3, 1]),
same_first_last([1, 2, 1]))