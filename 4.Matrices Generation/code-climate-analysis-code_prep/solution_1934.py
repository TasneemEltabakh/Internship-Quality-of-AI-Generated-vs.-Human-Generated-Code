# Python3 code to demonstrate working of
# Tuple List Kth Column Product
# using list comprehension + loop

# getting Product
def prod(val) :
res = 1
for ele in val:
res *= ele
return res

# initialize list
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Tuple List Kth Column Product
# using list comprehension + loop
res = prod([sub[K] for sub in test_list])

# printing result
print("Product of Kth Column of Tuple List : " + str(res))