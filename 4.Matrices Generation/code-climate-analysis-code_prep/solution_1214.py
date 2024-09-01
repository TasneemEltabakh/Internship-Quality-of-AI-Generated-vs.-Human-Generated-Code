def split_list(lst, n):
    result = list((lst[i:i+n] for i in range(0, len(lst), n)))
    return result
nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 3
print("\nSplit the said list into equal size",n)
print(split_list(nums,n))
n = 4
print("\nSplit the said list into equal size",n)
print(split_list(nums,n))
n = 5
print("\nSplit the said list into equal size",n)
print(split_list(nums,n))
