

'''Write a Python
programtofind the nth strong number. orWrite a
programtofind the nth strong number using Python '''

print("Enter the Nth value:")
rangenumber=int(input())
num = 1
c = 0
letest = 0

while (c != rangenumber):
  num2 = num
  num1 = num
  sum = 0
  fact = 1
  while (num1 != 0):
    fact = 1
    rem = num1 % 10
    num1 = num1 // 10
    for j in range(1,rem+1):
      fact = fact * j
    sum = sum + fact
  if (sum == num2):
    c+=1
    letest = num
  num = num + 1
print(rangenumber,"th strong number is ",letest)

