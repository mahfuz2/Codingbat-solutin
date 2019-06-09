def centered_average(nums):
  high = max(nums)
  low = min(nums)
  nums.remove(high)
  nums.remove(low)
  return int(sum(nums)/len(nums))

print(centered_average([1, 2, 3, 4, 100]),
centered_average([1, 1, 5, 5, 10, 8, 7]),
centered_average([-10, -4, -2, -4, -2, 0]))