# define the size (no. of columns)
# must be odd to draw proper diamond shape
size = 8


# initialize the spaces
spaces = size


# loops for iterations to create worksheet
for i in range(size//2+2):
for j in range(size):

# condition to left space
# condition to right space
# condition for making diamond
# else print *
if j < i-1:
print(' ', end=" ")
elif j > spaces:
print(' ', end=" ")
elif (i == 0 and j == 0) | (i == 0 and j == size-1):
print(' ', end=" ")
else:
print('*', end=" ")

# increase space area by decreasing spaces
spaces -= 1

# for line change
print()