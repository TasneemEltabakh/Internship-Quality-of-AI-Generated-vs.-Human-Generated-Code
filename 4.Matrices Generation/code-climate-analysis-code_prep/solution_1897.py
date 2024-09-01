# Python3 code to demonstrate working of
# Remove nested records
# using isinstance() + enumerate() + loop

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove nested records
# using isinstance() + enumerate() + loop
res = tuple()
for count, ele in enumerate(test_tup):
if not isinstance(ele, tuple):
res = res + (ele, )

# printing result
print("Elements after removal of nested records : " + str(res))