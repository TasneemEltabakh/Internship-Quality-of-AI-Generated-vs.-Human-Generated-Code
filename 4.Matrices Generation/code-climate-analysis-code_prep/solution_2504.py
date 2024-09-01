

'''Write a Python
programtofind the nth perfect number. orWrite a
programtofind the nth perfect number using Python '''


print("Enter a Nth Number:")
rangenumber=int(input())
c = 0
letest = 0
num = 1
while (c != rangenumber):
  sum = 0
  for i in range(num):
    if (num % i == 0):
    sum = sum + i

  if (sum == num):
    c+=1
    letest = num

  num = num + 1
print(rangenumber,"th perfect number is ",letest)

