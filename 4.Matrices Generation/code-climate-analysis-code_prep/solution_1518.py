def reverse_list_lists(nums):
    for l in nums:
        l.sort(reverse = True)
    return nums    
nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Original list of lists:")
print(nums)
print("\nReverse each list in the said list of lists:")
print(reverse_list_lists(nums))
