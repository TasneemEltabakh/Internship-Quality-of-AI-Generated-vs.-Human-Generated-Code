def most_frequent(nums):
  return max(set(nums), key = nums.count) 
print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))
nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
print ("Original list:")
print(nums)
print("Item with maximum frequency of the said list:")
print(most_frequent(nums))
nums = [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
print ("\nOriginal list:")
print(nums)
print("Item with maximum frequency of the said list:")
print(most_frequent(nums))
