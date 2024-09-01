def merge_some_chars(lst,merge_from,merge_to):
    result = lst
    result[merge_from:merge_to] = [''.join(result[merge_from:merge_to])]    
    return result    
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original lists:")
print(chars)
merge_from = 2
merge_to = 4
print("\nMerge items from",merge_from,"to",merge_to,"in the said List:")
print(merge_some_chars(chars,merge_from,merge_to))
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
merge_from = 3
merge_to = 7
print("\nMerge items from",merge_from,"to",merge_to,"in the said List:")
print(merge_some_chars(chars,merge_from,merge_to))
