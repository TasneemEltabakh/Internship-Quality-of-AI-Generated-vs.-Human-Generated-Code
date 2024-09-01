import itertools as it
def sum_pairs_list(nums, n):
    for num2, num1 in list(it.combinations(nums[::-1], 2))[::-1]:
        if num2 + num1 == n:
            return [num1, num2]

nums = [1,2,3,4,5,6,7]     
n = 10
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))

nums = [1,2,-3,-4,-5,6,-7]     
n = -6
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))
