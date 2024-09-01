def count_dups(nums):
    element = []
    freque = []
    if not nums:
        return element
    running_count = 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            running_count += 1
        else:
            freque.append(running_count)
            element.append(nums[i])
            running_count = 1
    freque.append(running_count)
    element.append(nums[i+1])
    return element,freque


nums = [1,2,2,2,4,4,4,5,5,5,5]
print("Original lists:")
print(nums)

print("\nConsecutive duplicate elements and their frequency:")
print(count_dups(nums))
