
str=input("Enter the String(Lower case):")
i=0
ch=''
#convert capital letter string to small letter string
while len(str)>i:
  if str[i]>='a' and str[i]<='z' :
    ch+=chr(ord(str[i])-32)
  else:
    ch += chr(ord(str[i]))
  i+=1
print("Lower case String is:", ch)