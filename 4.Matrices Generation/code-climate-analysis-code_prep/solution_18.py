def remove_last_n(nums, N):
    result = nums[:len(nums)-N]
    return result    
nums = [2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
print("Original lists:")
print(nums)
N = 3
print("\nRemove the last",N,"elements from the said list:")
print(remove_last_n(nums, N))
N = 5
print("\nRemove the last",N,"elements from the said list:")
print(remove_last_n(nums, N))
N = 1
print("\nRemove the last",N,"element from the said list:")
print(remove_last_n(nums, N))
