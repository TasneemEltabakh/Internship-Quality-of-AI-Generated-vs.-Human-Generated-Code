
row_size=int(input("Enter the row size:"))
for out in range(row_size+1):
  for i in range(1,out+1):
    print(i,end="")
  print("\r")
