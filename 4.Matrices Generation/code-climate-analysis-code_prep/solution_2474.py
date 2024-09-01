
rangenumber=int(input("Enter a Nth Number:"))
c = 0
letest = 0
num = 1
while c != rangenumber:
    sqr = num * num
    # Sum of digit
    sum = 0
    while sqr != 0:
      rem = sqr % 10
      sum += rem
      sqr //= 10

    if sum == num:
      c+=1
      letest = num

    num = num + 1
print(rangenumber,"th Magic number is ",latest)