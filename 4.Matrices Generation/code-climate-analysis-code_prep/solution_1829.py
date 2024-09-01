# Python3 code to demonstrate working of
# Convert tuple to float
# using join() + float() + str() + generator expression

# initialize tuple
test_tup = (4, 56)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Convert tuple to float
# using join() + float() + str() + generator expression
res = float('.'.join(str(ele) for ele in test_tup))

# printing result
print("The float after conversion from tuple is : " + str(res))