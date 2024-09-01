
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
  num3 = num
  num1 = num
  sum = 0
  # Sum of digit
  while num1 != 0:
    rem = num1 % 10
    sum += rem
    num1 //= 10
  # Reverse of sum
  rev = 0
  num2 = sum
  while num2 != 0:
    rem2 = num2 % 10
    rev = rev * 10 + rem2
    num2 //= 10
  if sum * rev == num3:
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th Magic number is ",letest)