

'''Write a Python
programtofind the nth prime number. orWrite a
programtofind the nth prime number using Python '''


print("Enter Nth Number:")
rangenumber=int(input())
c = 0
num = 2
letest = 0

while (c != rangenumber):
 count = 0
 for i in range(2,num):
   if (num % i == 0):
    count+=1
    break
 if (count == 0):
   c+=1
   letest = num
 num = num + 1
print (rangenumber,"th prime number is ",letest)
