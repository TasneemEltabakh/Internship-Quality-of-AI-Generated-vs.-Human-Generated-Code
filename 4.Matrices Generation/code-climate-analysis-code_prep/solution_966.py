def common_in_nested_lists(nested_list):
    result = list(set.intersection(*map(set, nested_list)))
    return result
nested_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print("\nOriginal lists:")
print(nested_list)
print("\nCommon element(s) in nested lists:")
print(common_in_nested_lists(nested_list))
