from typing import List

def binary_search(target: int, nums: List[int]=[]) -> int:
  l, h = 0, len(nums) - 1
  while l <= h:
    m = (l + h) // 2
    if target == nums[m]:
      return m
    elif target < nums[m]:
      h = m - 1
    else:
      l = m + 1 
  return -1

nums = [1, 2, 3, 4, 5, 6, 7]
target = int(input("What number do you want to find? "))
print(binary_search(target, nums))
