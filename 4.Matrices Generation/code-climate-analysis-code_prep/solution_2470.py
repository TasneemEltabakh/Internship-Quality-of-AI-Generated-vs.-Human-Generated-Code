
row_size=int(input("Enter the row size:"))
star_print=row_size*2-1
for out in range(row_size,0,-1):
  for inn in range(row_size,out,-1):
    print(" ",end="")
  for p in range(0,star_print):
    print("*",end="")
  star_print-=2
  print("\r")