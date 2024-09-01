nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Original list:", nums)
numbers=list(map(round,nums))
print("Minimum value: ",min(numbers))
print("Maximum value: ",max(numbers))
numbers=list(set(numbers))
numbers=(sorted(map(lambda n:n*5,numbers)))
print("Result:")
for numb in numbers:
    print(numb,end=' ')
