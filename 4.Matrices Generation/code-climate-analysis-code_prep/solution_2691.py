
row_size=int(input("Enter the row size:"))
star_print=1
for out in range(0,row_size):
  for inn in range(row_size-1,out,-1):
    print(" ",end="")
  for p in range(0,star_print):
    print("*",end="")
  star_print+=2
  print("\r")