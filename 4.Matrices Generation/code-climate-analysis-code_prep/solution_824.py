# Source: https://bit.ly/3qZqcwm
def almost_increasing_sequence(sequence):
    if len(sequence) < 3:
        return True

    a, b, *sequence = sequence
    skipped = 0
    for c in sequence:
        if a < b < c:  # XXX
            a, b = b, c
            continue
        elif b < c:    # !XX
            a, b = b, c
        elif a < c:    # X!X
            a, b = a, c
        skipped += 1
        if skipped == 2:
            return False
    return a < b

print(almost_increasing_sequence([]))
print(almost_increasing_sequence([1]))
print(almost_increasing_sequence([1, 2]))
print(almost_increasing_sequence([1, 2, 3]))
print(almost_increasing_sequence([3, 1, 2]))
print(almost_increasing_sequence([1, 2, 3, 0, 4, 5, 6]))
print(almost_increasing_sequence([1, 2, 3, 0]))
print(almost_increasing_sequence([1, 2, 0, 3]))
print(almost_increasing_sequence([10, 1, 2, 3, 4, 5]))
print(almost_increasing_sequence([1, 2, 10, 3, 4]))
print(almost_increasing_sequence([1, 2, 3, 12, 4, 5]))

print(almost_increasing_sequence([3, 2, 1]))
print(almost_increasing_sequence([1, 2, 0, -1]))
print(almost_increasing_sequence([5, 6, 1, 2]))
print(almost_increasing_sequence([1, 2, 3, 0, -1]))
print(almost_increasing_sequence([10, 11, 12, 2, 3, 4, 5]))
