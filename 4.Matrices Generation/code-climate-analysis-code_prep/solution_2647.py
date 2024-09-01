
print("Enter the row size:")
row_size=int(input())
for out in range(row_size+1):
  for j in range(row_size,out,-1):
    print("*",end="")
  print("\r")
