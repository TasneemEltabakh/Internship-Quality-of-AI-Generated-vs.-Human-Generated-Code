
row_size=int(input("Enter the row size:"))
for out in range(1,row_size+1):
  for i in range(row_size+1,out,-1):
    print(out,end="")
  print("\r")
