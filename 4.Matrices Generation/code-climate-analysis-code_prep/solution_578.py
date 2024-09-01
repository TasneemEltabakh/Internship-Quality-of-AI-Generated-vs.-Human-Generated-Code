def comb_sort(nums):
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)

        swapped = False
        i = 0

        while gaps + i < len(nums):
            if nums[i] > nums[i+gaps]:
                nums[i], nums[i+gaps] = nums[i+gaps], nums[i]
                swapped = True
            i += 1
    return nums

num1 = input('Input comma separated numbers:\n').strip()
nums = [int(item) for item in num1.split(',')]
print(comb_sort(nums))
