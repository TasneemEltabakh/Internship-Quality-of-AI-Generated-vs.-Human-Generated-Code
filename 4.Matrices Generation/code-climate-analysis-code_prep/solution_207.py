def test(lst):
    result = [x + y for x, y in zip(lst[::2],lst[1::2])]
    return result

nums = ['1','2','3','4','5','6','7','8']
print("Original list:")
print(nums)
print("\nJoin adjacent members of a given list:")
print(test(nums))

nums = ['1','2','3']
print("\nOriginal list:")
print(nums)
print("\nJoin adjacent members of a given list:")
print(test(nums))
