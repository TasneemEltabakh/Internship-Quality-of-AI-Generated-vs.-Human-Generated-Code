
row_size=int(input("Enter the row size:"))
print_control_x=row_size
print_control_y=row_size
for out in range(1,row_size+1):
  for inn in range(1,row_size*2):
    if inn>print_control_x and inn<print_control_y:
      print(" ",end="")
    else:
      print("*", end="")
  print_control_x-=1
  print_control_y+=1
  print("\r")