# Python3 code to demonstrate working of
# Convert Binary tuple to Integer
# Using join() + list comprehension + int()

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# using int() with base to get actual number
res = int("".join(str(ele) for ele in test_tup), 2)

# printing result
print("Decimal number is : " + str(res))