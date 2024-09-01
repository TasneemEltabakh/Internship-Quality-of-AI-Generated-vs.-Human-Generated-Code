import itertools as it
import operator as op

def factorials_nums(n):
    result = list(it.accumulate(it.chain([1], range(1, 1 + n)), op.mul))
    return result;
    
 
print("Factorials of 5 :", factorials_nums(5))
print("Factorials of 9 :", factorials_nums(9))
