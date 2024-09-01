def test_dsc(n):
    return int(''.join(sorted(str(n), reverse = True)))

def test_asc(n):
    return int(''.join(sorted(list(str(n))))[::1])

n = 134543
print("Original Number: ",n);
print("Descending order of the said number: ", test_dsc(n));
print("Ascending order of the said number: ", test_asc(n));
n = 43750973
print("\nOriginal Number: ",n);
print("Descending order of the said number: ", test_dsc(n));
print("Ascending order of the said number: ", test_asc(n));
