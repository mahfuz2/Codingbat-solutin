def big_diff(nums):
  a = max(nums)
  b = min(nums)
  return a-b

print(big_diff([10, 3, 5, 6]),
big_diff([7, 2, 10, 9]),
big_diff([2, 10, 7, 2]) )