#Source: shorturl.at/csxLM
def test(list1):
    result =   [(x + y) / 2.0 for (x, y) in zip(list1[:-1], list1[1:])]
    return list(result)

nums =  [1,2,3,4,5,6,7]
print("\nOriginal list:")
print(nums)
print("\nSum the said list of numbers:")
print(test(nums))

nums =  [0,1,-3,3,7,-5,6,7,11]
print("\nOriginal list:")
print(nums)
print("\nSum the said list of numbers:")
print(test(nums))
