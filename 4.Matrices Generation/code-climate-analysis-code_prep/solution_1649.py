def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result

nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print ("Original list:")
print(nums)
print("\nItem with maximum occurrences of the said list:")
print(max_occurrences(nums)) 
