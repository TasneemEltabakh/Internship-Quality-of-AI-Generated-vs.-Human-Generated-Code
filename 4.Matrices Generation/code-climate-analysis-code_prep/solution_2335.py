# Python implementation of converting
# a string into a dictionary

# initialising string
str = " Jan = January; Feb = February; Mar = March"

# At first the string will be splitted
# at the occurence of ';' to divide items
# for the dictionaryand then again splitting
# will be done at occurence of '=' which
# generates key:value pair for each item
dictionary = dict(subString.split("=") for subString in str.split(";"))

# printing the generated dictionary
print(dictionary)