# Function to find lost element from a duplicate
# array

def lostElement(A,B):

# convert lists into set
A = set(A)
B = set(B)

# take difference of greater set with smaller
if len(A) > len(B):
print (list(A-B))
else:
print (list(B-A))

# Driver program
if __name__ == "__main__":
A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
lostElement(A,B)