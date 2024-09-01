
print("Enter the row and column size:");
row_size=int(input())
for out in range(1,row_size+1):
  for i in range(0,row_size):
    print(out,end="")
  print("\r")