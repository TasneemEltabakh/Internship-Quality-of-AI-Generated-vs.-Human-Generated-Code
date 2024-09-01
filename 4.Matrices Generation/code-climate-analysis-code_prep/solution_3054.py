
print("Enter a range:")
range1=int(input())
range2=int(input())
print("Neon numbers between ",range1," and ",range2," are: ")
for i in range(range1,range2+1):
  sqr =i*i
  # Sum of digit
  sum = 0
  while sqr != 0:
    rem = sqr % 10
    sum += rem
    sqr //= 10

  if sum == i:
    print(i,end=" ")