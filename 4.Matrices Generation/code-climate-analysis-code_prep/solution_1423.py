#Ref.https://bit.ly/36fvcEw
def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)
def three_way_radix_quicksort(sorting: list) -> list:
    if len(sorting) <= 1:
        return sorting
    return (
        three_way_radix_quicksort([i for i in sorting if i < sorting[0]])
        + [i for i in sorting if i == sorting[0]]
        + three_way_radix_quicksort([i for i in sorting if i > sorting[0]])
    )
nums = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(nums)
print("After applying Random Pivot Quick Sort the said list becomes:")
quick_sort_3partition(nums, 0, len(nums)-1)
print(nums)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(nums)
print("After applying Multi-key quicksort the said list becomes:")
quick_sort_3partition(nums, 0,  len(nums)-1)
print(nums)
nums = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(nums)
print("After applying Multi-key quicksort the said list becomes:")
quick_sort_3partition(nums, 0, len(nums)-1)
print(nums)
nums = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(nums)
print("After applying Multi-key quicksort the said list becomes:")
quick_sort_3partition(nums, 1,  len(nums)-1)
print(nums)
nums = ['z','a','y','b','x','c']
print("\nOriginal list:")
print(nums)
print("After applying Multi-key quicksort the said list becomes:")
quick_sort_3partition(nums, 0, len(nums)-1)
print(nums)
nums = ['z','a','y','b','x','c']
print("\nOriginal list:")
print(nums)
print("After applying Multi-key quicksort the said list becomes:")
quick_sort_3partition(nums, 2,  len(nums)-1)
print(nums) 
