
row_size=int(input("Enter the row size:"))
for out in range(row_size,0,-1):
  for in1 in range(row_size,out,-1):
    print(" ",end="")
  for in2 in range(1, out+1):
    print(in2,end="")
  print("\r")
