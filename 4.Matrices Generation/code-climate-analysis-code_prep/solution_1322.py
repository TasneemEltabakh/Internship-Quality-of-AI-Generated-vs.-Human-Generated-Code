def sum_lists_diff_length(test_list):
    result =  [sum(x) for x in zip(*map(lambda x:x+[0]*max(map(len, test_list)) if len(x)<max(map(len, test_list)) else x, test_list))]
    return result

nums = [[1,2,4],[2,4,4],[1,2]]
print("\nOriginal list:")
print(nums)
print("Sum said lists with different lengths:")
print(sum_lists_diff_length(nums))

nums = [[1],[2,4,4],[1,2],[4]]
print("\nOriginal list:")
print(nums)
print("Sum said lists with different lengths:")
print(sum_lists_diff_length(nums))
