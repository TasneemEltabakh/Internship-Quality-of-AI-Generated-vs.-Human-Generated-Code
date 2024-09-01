# Python3 code to demonstrate working of
# Similar characters Strings comparison
# Using split() + sorted()

# initializing strings
test_str1 = 'e:e:k:s:g'
test_str2 = 'g:e:e:k:s'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing delim
delim = ':'

# == operator is used for comparison
res = sorted(test_str1.split(':')) == sorted(test_str2.split(':'))

# printing result
print("Are strings similar : " + str(res))