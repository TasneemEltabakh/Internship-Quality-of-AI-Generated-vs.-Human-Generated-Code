def first_even_odd(nums):
    first_even = next((el for el in nums if el%2==0),-1)
    first_odd = next((el for el in nums if el%2!=0),-1)
    return first_even,first_odd

nums= [1,3,5,7,4,1,6,8]
print("Original list:")
print(nums)
print("\nFirst even and odd number of the said list of numbers:")
print(first_even_odd(nums))
