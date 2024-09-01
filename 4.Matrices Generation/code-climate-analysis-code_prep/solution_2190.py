# importing required libraries
import numpy


# explicit function to compute column wise sum
def colsum(arr, n, m):
for i in range(n):
su = 0;
for j in range(m):
su += arr[j][i]
print(su, end = " ")


# creating the 2D Array
TwoDList = [[1, 2, 3], [4, 5, 6],
[7, 8, 9], [10, 11, 12]]
TwoDArray = numpy.array(TwoDList)


# displaying the 2D Array
print("2D Array:")
print(TwoDArray)


# printing the sum of each column
print("\nColumn-wise Sum:")
colsum(TwoDArray, len(TwoDArray[0]), len(TwoDArray))