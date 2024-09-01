
row_size=int(input("Enter the row size:"))
for out in range(row_size,-row_size,-1):
  for in1 in range(1,abs(out)+1):
    print(" ",end="")
  for in2 in range(row_size,abs(out),-1):
    print("* ",end="")
  print("\r")
