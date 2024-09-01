
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num2=0
  num1 = num
  while num1 != 0:
    rem = num1 % 10
    num1 //= 10
    num2 = num2 * 10 + rem
  if num==num2:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Palindrome Number is ",letest)