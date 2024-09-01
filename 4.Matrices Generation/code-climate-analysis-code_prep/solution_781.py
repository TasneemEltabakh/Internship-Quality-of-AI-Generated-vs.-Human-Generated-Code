def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p
nums = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",nums)
print("Product of the unique numbers of the said list: ",unique_product(nums))
