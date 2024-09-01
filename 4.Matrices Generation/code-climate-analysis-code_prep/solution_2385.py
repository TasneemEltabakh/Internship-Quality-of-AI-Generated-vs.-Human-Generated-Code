# Python3 code to demonstrate working of
# Replace all Characters Except K
# Using list comprehension and conditional expressions

# initializing lists
test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']

# printing original list
print("The original list : " + str(test_list))

# initializing repl_chr
repl_chr = '$'

# initializing retain chararter
ret_chr = 'G'

# list comprehension to remake list after replacement
res = [ele if ele == ret_chr else repl_chr for ele in test_list]

# printing result
print("List after replacement : " + str(res))