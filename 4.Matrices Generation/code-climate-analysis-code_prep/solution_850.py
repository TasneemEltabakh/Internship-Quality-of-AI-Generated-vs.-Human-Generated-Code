from collections.abc import Iterable
def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
nums = [1, [2], [[3], [4], 5], 6]
print("Original list elements:")
print(nums) 
print()
print("Deep flatten the said list:")
print(deep_flatten(nums))
nums = [[[1, 2, 3], [4, 5]], 6]
print("\nOriginal list elements:")
print(nums) 
print()
print("Deep flatten the said list:")
print(deep_flatten(nums))
