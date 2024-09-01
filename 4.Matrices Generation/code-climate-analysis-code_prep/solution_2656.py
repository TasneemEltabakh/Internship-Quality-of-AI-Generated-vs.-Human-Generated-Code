
size=int(input("Enter number of names:"))
print("Enter ",size," names:")
str=[]
for i in range(size):
  ele=input()
  str.append(ele)
for i in range(size):
  for j in range(i+1,size):
       if (str[i]>str[j])>0:
         temp=str[i]
         str[i]=str[j]
         str[j]=temp
print("After sorting names are:")
for i in range(size):
  print(str[i])