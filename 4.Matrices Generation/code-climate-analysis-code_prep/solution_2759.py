
row_size=int(input("Enter the row size:"))
np=1
for out in range(0,row_size):
  for in1 in range(row_size-1,out,-1):
    print(" ",end="")
  for in2 in range(np,0,-1):
    print(in2,end="")
  np+=2
  print("\r")
