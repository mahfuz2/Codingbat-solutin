def max_end3(nums):
  max = nums[0]
  if nums[2]>max:
    max = nums[2]
  return [max,max,max]

print(max_end3([1, 2, 3]),
max_end3([11, 5, 9]),
max_end3([2, 11, 3]))