def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())

nums = [10,2,56]
print("Original tuple: ") 
print(nums)
print("Sum of digits of each number of the said list of integers:")
print(sum_of_digits(nums))

nums = [10,20,4,5,'b',70,'a']
print("\nOriginal tuple: ") 
print(nums)
print("Sum of digits of each number of the said list of integers:")
print(sum_of_digits(nums))

nums = [10,20,-4,5,-70]
print("\nOriginal tuple: ") 
print(nums)
print("Sum of digits of each number of the said list of integers:")
print(sum_of_digits(nums))
