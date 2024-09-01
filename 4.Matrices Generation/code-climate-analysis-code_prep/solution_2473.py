
print("Enter the range of number(Limit):")
n = int(input())
i = 1
sum = 0
while (i <= n):
  for j in range(1, i + 1,2):
    sum+=j
  i += 2
print("The sum of the series = ", sum)