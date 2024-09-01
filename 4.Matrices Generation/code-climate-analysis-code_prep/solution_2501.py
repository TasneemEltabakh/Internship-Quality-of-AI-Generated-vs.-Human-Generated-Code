
row_size=int(input("Enter the row size:"))
print_control_x=row_size//2+1
for out in range(1,row_size+1):
  for inn in range(1,row_size+1):
    if inn==print_control_x or inn==row_size-print_control_x+1:
      print("*",end="")
    else:
      print(" ", end="")
  if out <= row_size // 2:
    print_control_x-=1
  else:
    print_control_x+=1
  print("\r")