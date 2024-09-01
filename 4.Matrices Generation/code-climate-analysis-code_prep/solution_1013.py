def test(lst):
    previous_digit = 0
    ctr = 0
    for digit in lst:
        if previous_digit==0 and digit!=0:
            ctr+=1
        previous_digit = digit
    return ctr

nums = [3,4,6,2,0,0,0,0,0,0,6,7,6,9,10,0,0,0,0,0,5,9,9,7,4,4,0,0,0,0,0,0,5,3,2,9,7,1]

print("\nOriginal list:")
print(nums)
print("\nNumber of groups of non-zero numbers separated by zeros of the said list:")
print(test(nums)) 
