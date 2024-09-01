
row_size=int(input("Enter the row size:"))
for out in range(row_size,-(row_size-1),-1):
  for i in range((row_size),abs(out-1),-1):
    print("*",end="")
  print("\r")

