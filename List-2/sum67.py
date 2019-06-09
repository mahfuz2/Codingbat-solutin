def sum67(nums):
  sum = 0
  found = False
  for i in range(len(nums)):
    if nums[i]==6:
      found =True
    if not found:
      sum = sum +nums[i]
    if nums[i]==7 and found:
      found = False
  return sum

print(sum67([1, 2, 2]),
sum67([1, 2, 2, 6, 99, 99, 7]),
sum67([1, 1, 6, 7, 2]))