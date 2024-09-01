# Python3 code to demonstrate working of
# Possible Substring count from String
# Using min() + list comprehension + count()


# initializing string
test_str = "gekseforgeeks"


# printing original string
print("The original string is : " + str(test_str))


# initializing arg string
arg_str = "geeks"


# using min and count to get minimum possible
# occurrence of character
res = min(test_str.count(char) // arg_str.count(char) for char in set(arg_str))


# printing result
print("Possible substrings count : " + str(res))