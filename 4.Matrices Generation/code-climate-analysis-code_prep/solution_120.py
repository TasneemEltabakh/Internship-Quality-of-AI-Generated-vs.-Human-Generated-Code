#Ref.https://bit.ly/3oneU2l
def bubble_sort(list_data: list, length: int = 0) -> list:
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else bubble_sort(list_data, length - 1)
nums = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(nums)
print("After applying Recursive Insertion Sort the said list becomes:")
bubble_sort(nums, len(nums))
print(nums)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(nums)
print("After applying Recursive Bubble Sort the said list becomes:")
bubble_sort(nums, len(nums))
print(nums)
nums = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(nums)
print("After applying Recursive Bubble Sort the said list becomes:")
bubble_sort(nums, len(nums))
print(nums)
nums = ['z','a','y','b','x','c']
print("\nOriginal list:")
print(nums)
print("After applying Recursive Bubble Sort the said list becomes:")
bubble_sort(nums, len(nums))
print(nums)
