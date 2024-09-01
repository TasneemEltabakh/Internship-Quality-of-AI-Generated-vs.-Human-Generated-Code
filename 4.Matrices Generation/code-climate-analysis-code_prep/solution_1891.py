# importing numpy as np
import numpy as np


# creating array of string
x = np.array(["geeks", "for", "geeks"],
dtype=np.str)
print("Printing the Original Array:")
print(x)

# inserting space using np.char.join()
r = np.char.join(" ", x)
print("Printing the array after inserting space\
between the elements")
print(r)