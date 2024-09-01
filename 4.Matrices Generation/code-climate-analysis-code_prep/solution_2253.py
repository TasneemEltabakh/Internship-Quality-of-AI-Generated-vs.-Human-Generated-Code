# Function to rearrange positive and negative elements
def Rearrange(arr):

# First lambda expression returns list of negative numbers
# in arr.
# Second lambda expression returns list of positive numbers
# in arr.
return [x for x in arr if x < 0] + [x for x in arr if x >= 0]

# Driver function
if __name__ == "__main__":
arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
print (Rearrange(arr))