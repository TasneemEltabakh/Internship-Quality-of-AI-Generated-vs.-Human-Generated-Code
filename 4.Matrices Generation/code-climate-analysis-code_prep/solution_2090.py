def func():

# defining local variable
a_variable = 0

# using locals() function
# for checking existence in symbol table
is_local_var = "a_variable" in locals()

# printing result
print(is_local_var)

# driver code
func()