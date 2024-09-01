import itertools

def max_sub_string(str1):
    return max(len(list(x)) for _, x in itertools.groupby(str1))
    
    
str1 = "aaabbccddeeeee"

print("Original string:",str1)
print("Maximum length of a substring with unique characters of the said string:")
print(max_sub_string(str1))

str1 = "c++ exercises"
print("\nOriginal string:",str1)
print("Maximum length of a substring with unique characters of the said string:")
print(max_sub_string(str1))
