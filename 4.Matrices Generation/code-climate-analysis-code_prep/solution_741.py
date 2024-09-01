def wiggle_sort(arra_nums):
    for i, _ in enumerate(arra_nums):
        if (i % 2 == 1) == (arra_nums[i - 1] > arra_nums[i]):
            arra_nums[i - 1], arra_nums[i] = arra_nums[i], arra_nums[i - 1]

    return arra_nums

print("Input the array elements: ")
arra_nums = list(map(int, input().split()))
print("Original unsorted array:")
print(arra_nums)
print("The said array after applying Wiggle sort:")
print(wiggle_sort(arra_nums))
