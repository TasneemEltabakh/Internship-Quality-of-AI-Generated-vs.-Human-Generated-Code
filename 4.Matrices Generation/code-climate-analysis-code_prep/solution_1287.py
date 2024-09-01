from itertools import takewhile
def first_index(l1, n):
    return len(list(takewhile(lambda x: x[1] <= n, enumerate(l1))))


nums = [12,45,23,67,78,90,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 73
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))
n = 21
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))
n = 80
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))
n = 55
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))
