def remove_none(nums):
    result = [x for x in nums if x is not None]
    return result
nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print("Original list:")
print(nums)
print("\nRemove None value from the said list:")
print(remove_none(nums))
