# importing the module
from types import FunctionType

# functttion during run-time
f_code = compile('def gfg(): return "GEEKSFORGEEKS"', "<string>", "exec")
f_func = FunctionType(f_code.co_consts[0], globals(), "gfg")

# calling the function
print(f_func())