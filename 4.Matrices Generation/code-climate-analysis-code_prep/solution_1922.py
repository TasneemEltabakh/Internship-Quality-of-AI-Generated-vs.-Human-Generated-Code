def power(N, P):

# if power is 0 then return 1
if P == 0:
return 1

# if power is 1 then number is
# returned
elif P == 1:
return N

else:
return (N*power(N, P-1))

# Driver program
N = 5
P = 2

print(power(N, P))