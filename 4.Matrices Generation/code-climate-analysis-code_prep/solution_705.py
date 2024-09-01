def test(lst):
    result = all(str(x)[0] == str(lst[0])[0] for x in lst) 
    return result
nums = [1234, 122, 1984, 19372, 100]
print("\nOriginal list:")
print(nums)
print("Check if first digit in each element of the said given list is same or not!")
print(test(nums))
nums = [1234, 922, 1984, 19372, 100]
print("\nOriginal list:")
print(nums)
print("Check if first digit in each element of the said given list is same or not!")
print(test(nums))
nums = ['aabc', 'abc', 'ab', 'a']
print("\nOriginal list:")
print(nums)
print("Check if first character in each element of the said given list is same or not!")
print(test(nums))
nums = ['aabc', 'abc', 'ab', 'ha']
print("\nOriginal list:")
print(nums)
print("Check if first character in each element of the said given list is same or not!")
print(test(nums))
