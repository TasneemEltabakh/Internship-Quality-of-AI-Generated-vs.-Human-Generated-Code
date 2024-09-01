
row_size=int(input("Enter the row size:"))
np=1
for out in range(0,row_size):
  for in1 in range(row_size-1,out,-1):
    print(" ",end="")
  for in2 in range(0, np):
    print(np-out,end="")
  np+=2
  print("\r")
