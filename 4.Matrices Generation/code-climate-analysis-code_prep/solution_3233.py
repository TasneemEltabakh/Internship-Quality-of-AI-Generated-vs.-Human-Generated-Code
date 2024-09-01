
arr=[]
size = int(input("Enter the size of the array: "))
print("Enter the Element of the array:")
for i in range(0,size):
  num = float(input())
  arr.append(num)
sum_pos=0.0
sum_neg=0.0
for j in range(0,size):
    if (arr[j] > 0):
      sum_pos += arr[j]
    else:
      sum_neg += arr[j]
print("sum of positive number : ",sum_pos)
print("sum of Negative number : ",sum_neg)