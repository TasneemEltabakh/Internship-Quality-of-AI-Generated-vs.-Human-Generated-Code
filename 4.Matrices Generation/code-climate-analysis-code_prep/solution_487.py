def test(lst, value):
    result = [i for i,val in enumerate(lst) if val > value]
    return result
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print("\nOriginal list:")
print(nums)
val = 3000
print("Indices of elements of the said list, greater than",val)
print(test(nums,val))
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print("\nOriginal list:")
print(nums)
val = 20000
print("Indices of elements of the said list, greater than",val)
print(test(nums,val))
