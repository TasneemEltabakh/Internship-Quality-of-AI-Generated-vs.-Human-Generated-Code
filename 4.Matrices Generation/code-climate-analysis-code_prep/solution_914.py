from itertools import groupby
def count_same_pair(nums):
    result = [sum(1 for _ in group) for _, group in groupby(nums)]
    return result

nums = [1,1,2,2,2,4,4,4,5,5,5,5]
print("Original lists:")
print(nums)
print("\nFrequency of the consecutive duplicate elements:")
print(count_same_pair(nums))
