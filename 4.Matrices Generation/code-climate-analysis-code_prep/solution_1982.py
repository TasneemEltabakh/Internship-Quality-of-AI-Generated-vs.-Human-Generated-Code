# Python3 code to demonstrate working of
# Removing punctuations in string
# Using loop + punctuation string


# initializing string
test_str = "Gfg, is best : for ! Geeks ;"


# printing original string
print("The original string is : " + test_str)


# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
if ele in punc:
test_str = test_str.replace(ele, "")


# printing result
print("The string after punctuation filter : " + test_str)