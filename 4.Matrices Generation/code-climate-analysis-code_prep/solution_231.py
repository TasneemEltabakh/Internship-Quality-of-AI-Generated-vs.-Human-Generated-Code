def tuple_max_val(nums):
    result_max = max([abs(x * y) for x, y in nums] )
    result_min = min([abs(x * y) for x, y in nums] )
    return result_max,result_min
nums = [(2, 7), (2, 6), (1, 8), (4, 9)]   
print("The original list, tuple : ") 
print(nums)
print("\nMaximum and minimum product from the pairs of the said tuple of list:")
print(tuple_max_val(nums)) 
