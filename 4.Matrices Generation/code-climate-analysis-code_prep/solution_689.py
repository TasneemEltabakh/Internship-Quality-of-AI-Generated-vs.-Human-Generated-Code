from decimal import Decimal
#Source: https://bit.ly/3hEyyY4

def round_to_10_cents(x):
    remainder = x.remainder_near(Decimal('0.10'))
    if abs(remainder) == Decimal('0.05'):
        return x
    else:
        return x - remainder

# Test code.
for x in range(80, 120):
    y = Decimal(x) / Decimal('1E2')
    print("{0} rounds to {1}".format(y, round_to_10_cents(y)))
