

'''Write a Python
programtoCalculate Amicable pairs. orWrite a
programtoCalculate Amicable pairs using Python '''

print("Enter the two number:")
num1=int(input())
num2=int(input())
sum1=0;
sum2=0;
for i in range(1,num1):
  if num1%i==0:
    sum1+=i
for i in range(1,num2):
  if num2%i==0:
    sum2+=i
if sum1==num2:
  if sum2==num1:
    print("This is an amicable pair.")
else:
   print("This is not an amicable pair.")
