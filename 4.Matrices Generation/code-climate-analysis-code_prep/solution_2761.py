

'''Write a Python
programtoFind the Generic root of a number.''

print("Enter a number:")
num = int(input())
while num > 10:
  sum = 0
  while num:
    r=num % 10
    num= num / 10
    sum+= r
  if sum > 10:
    num = sum
  else:
    break
print("Generic root of the number is ", int(sum))
