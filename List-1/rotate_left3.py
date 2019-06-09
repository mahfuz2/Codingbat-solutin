def rotate_left3(nums):
  a = nums[0]
  for i in range(len(nums)-1):
    nums[i]=nums[i+1]
  nums[-1]=a
  return nums

print(rotate_left3([1, 2, 3]),
rotate_left3([5, 11, 9]),
rotate_left3([7, 0, 0]))