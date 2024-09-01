from collections import Counter
def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ] 
print(find_parity_outliers([1, 2, 3, 4, 6]))  
print(find_parity_outliers([1, 2, 3, 4, 5, 6, 7]))
