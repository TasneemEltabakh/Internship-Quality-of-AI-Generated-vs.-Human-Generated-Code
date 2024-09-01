
def reverse(num):
  if num<10:
   print(num)
   return
  else:
    print(num % 10,end="")
    reverse(int(num / 10))
print("Enter your number:")
num=int(input())
print("Reverse of the input number is:")
reverse(num)
