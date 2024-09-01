

print("Enter a HexaDecimal number:")
hex=input()
binary=""
i=0
j=1
for i in range(0,len(hex)):
  if hex[i]=='F' :
    binary=binary+"1111"
  elif hex[i]=="E":
    binary=binary+"1110"
  elif hex[i]=="D":
    binary=binary+"1101"
  elif hex[i]=="C":
    binary=binary+"1100"
  elif hex[i]=="B":
    binary=binary+"1011"
  elif hex[i]=="A":
    binary=binary+"1010"
  else:
    st=hex[i:i+1]
    decimal=0
    temp=1
    hexnum=int(st)
    while hexnum!=0:
      remainder=hexnum%2
      hexnum=hexnum//2
      decimal=decimal+remainder*temp
      temp=temp*10
    str1=str(decimal)
    if len(str1)==3:
      str1="0"+str1
    if len(str1)==2:
      str1="00"+str1
    if len(str1)==1:
      str1="000"+str1
    binary=binary+str1
print("HexaDecimal to Binary is",binary)
