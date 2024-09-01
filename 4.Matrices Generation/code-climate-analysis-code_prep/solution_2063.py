# Python program to capitalize
# first and last character of
# each word of a String


# Function to do the same
def word_both_cap(str):

#lamda function for capitalizing the
# first and last letter of words in
# the string
return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
s.title().split()))


# Driver's code
s = "welcome to geeksforgeeks"
print("String before:", s)
print("String after:", word_both_cap(str))