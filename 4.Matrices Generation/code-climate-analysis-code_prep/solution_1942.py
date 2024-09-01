# import library
import os

# take Input from the user
query = input("Which drive you have to open ? C , D or E: \n")

# Check the condition for
# opening the C drive
if "C" in query or "c" in query:
os.startfile("C:")

# Check the condition for
# opening the D drive
elif "D" in query or "d" in query:
os.startfile("D:")

# Check the condition for
# opening the D drive
elif "E" in query or "e" in query:
os.startfile("E:")

else:
print("Wrong Input")