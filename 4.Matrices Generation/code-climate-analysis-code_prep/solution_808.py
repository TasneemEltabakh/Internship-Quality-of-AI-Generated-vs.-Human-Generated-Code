#Ref.https://bit.ly/3a657IZ
from __future__ import annotations
import re
def natural_sort(input_list: list[str]) -> list[str]:
    def alphanum_key(key):
        return [int(s) if s.isdigit() else s.lower() for s in re.split("([0-9]+)", key)]
    return sorted(input_list, key=alphanum_key)
strs = ['2 ft 7 in', '1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '7 ft 6 in']
print("\nOriginal list:")
print(strs)
natural_sort(strs)
print("Sorted order is:", strs)
strs =  ['1 ft 5 in', '10 ft 2 in', '2 ft 11 in', '2 ft 7 in', '7 ft 6 in']
print("\nOriginal list:")
print(strs)
natural_sort(strs)
print("Sorted order is:", strs)
strs =  ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
print("\nOriginal list:")
print(strs)
natural_sort(strs)
print("Sorted order is:", strs)
strs =   ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
print("\nOriginal list:")
print(strs)
natural_sort(strs)
print("Sorted order is:", strs) 
